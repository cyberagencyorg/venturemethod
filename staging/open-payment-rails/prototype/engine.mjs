/**
 * SYNTHETIC, OFFLINE PROOF ONLY. No bank integration, cryptographic signature validation,
 * durable storage, authorization, transactional concurrency, compliance review or real funds.
 * The authenticated field is a mocked adapter result, never trust this flag from an HTTP client.
 * All state transitions are in memory. Production needs a DB transaction and unique constraints.
 * Run: node --test engine.test.mjs (Node 18+).
 */
export function reconcile(state, credit) {
  const next={payments:state.payments.map(p=>({...p})),credits:[...state.credits],allocations:[...state.allocations],events:[...state.events],exceptions:[...state.exceptions],outbox:[...state.outbox]};
  function incident(reason) {
    next.exceptions.push({id:"exc_"+(next.exceptions.length+1),reason,merchantId:credit?.merchantId??null,bankTransactionId:credit?.bankTransactionId??null});
    return {state:next,outcome:"EXCEPTION",reason};
  }
  if (!credit || typeof credit!=="object") return incident("INVALID_EVENT");
  const validId=x=>typeof x==="string"&&x.length>0;
  if(!validId(credit.merchantId)||!validId(credit.bankId)||!validId(credit.accountId)||!validId(credit.bankTransactionId)||!validId(credit.reference)|| !Number.isSafeInteger(credit.amountMinor)||credit.amountMinor<=0||!(/^[A-Z]{3}$/.test(credit.currency??""))||!(/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(credit.occurredAt??""))) return incident("INVALID_EVENT");
  if(credit.authenticated!==true || !["BANK_DIRECT","AUTHORIZED_BANK_DELEGATE"].includes(credit.evidenceLevel)) return incident("UNTRUSTED_SOURCE");
  const key=JSON.stringify([credit.merchantId,credit.bankId,credit.accountId,credit.bankTransactionId]);
  const fingerprint=JSON.stringify([credit.amountMinor,credit.currency,credit.reference,credit.occurredAt,credit.evidenceLevel]);
  const prior=next.credits.find(c=>c.key===key);
  if(prior) {
    if(prior.fingerprint!==fingerprint) return incident("CONFLICTING_DUPLICATE");
    return {state:next,outcome:"REPLAY",reason:null};
  }
  next.credits.push({key,fingerprint,merchantId:credit.merchantId,bankId:credit.bankId,accountId:credit.accountId,bankTransactionId:credit.bankTransactionId,amountMinor:credit.amountMinor,currency:credit.currency,reference:credit.reference,occurredAt:credit.occurredAt,evidenceLevel:credit.evidenceLevel});
  const allReferences=next.payments.filter(p=>p.merchantId===credit.merchantId&&p.reference===credit.reference);
  const candidates=next.payments.filter(p=>p.merchantId===credit.merchantId && p.bankId===credit.bankId && p.accountId===credit.accountId && p.currency===credit.currency && p.amountMinor===credit.amountMinor && p.reference===credit.reference && p.status==="AWAITING_PAYMENT" && (!p.expiresAt||credit.occurredAt<=p.expiresAt));
  if(candidates.length>1) return incident("AMBIGUOUS_MATCH");
  if(candidates.length===0) {
    const r=allReferences.some(p=>p.status==="PAID")?"ALREADY_PAID":allReferences.some(p=>p.status==="CANCELED")?"CANCELED_REQUEST":allReferences.some(p=>p.expiresAt&&credit.occurredAt>p.expiresAt)?"LATE_PAYMENT":allReferences.length>0?"MISMATCHED_PAYMENT":"NO_EXACT_MATCH";
    return incident(r);
  }
  const match=candidates[0];
  if(next.allocations.some(a=>a.paymentId===match.paymentId||a.creditKey===key)) return incident("ALLOCATION_CONFLICT");
  next.payments=next.payments.map(p=>p.paymentId===match.paymentId?{...p,status:"PAID"}:p);
  const eventId="payment.verified:"+match.paymentId;
  next.allocations.push({creditKey:key,paymentId:match.paymentId,amountMinor:credit.amountMinor,currency:credit.currency});
  next.events.push({eventId,type:"payment.verified",paymentId:match.paymentId,creditKey:key,evidenceLevel:credit.evidenceLevel});
  next.outbox.push({eventId,deliveryStatus:"PENDING"});
  return {state:next,outcome:"PAID",paymentId:match.paymentId,reason:null};
}
