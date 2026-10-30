import test from "node:test";
import assert from "node:assert/strict";
import { reconcile } from "./engine.mjs";
const baseP={"paymentId":"p1","merchantId":"m1","bankId":"B1","accountId":"A1","amountMinor":12000,"currency":"VND","reference":"INV001","expiresAt":"2026-10-31T00:00:00Z","status":"AWAITING_PAYMENT"};
const baseC={"merchantId":"m1","bankId":"B1","accountId":"A1","bankTransactionId":"TX001","amountMinor":12000,"currency":"VND","reference":"INV001","occurredAt":"2026-10-30T00:00:00Z","authenticated":true,"evidenceLevel":"BANK_DIRECT"};
function fresh(ps){return {payments:ps.map(p=>({...p})),credits:[],allocations:[],events:[],exceptions:[],outbox:[]};}
const cases=[
  {
    "name": "exact valid credit",
    "ps": [
      {}
    ],
    "credit": {},
    "out": "PAID"
  },
  {
    "name": "wrong amount",
    "ps": [
      {}
    ],
    "credit": {
      "amountMinor": 12001
    },
    "out": "EXCEPTION",
    "reason": "MISMATCHED_PAYMENT"
  },
  {
    "name": "wrong currency",
    "ps": [
      {}
    ],
    "credit": {
      "currency": "THB"
    },
    "out": "EXCEPTION",
    "reason": "MISMATCHED_PAYMENT"
  },
  {
    "name": "wrong bank account",
    "ps": [
      {}
    ],
    "credit": {
      "accountId": "A2"
    },
    "out": "EXCEPTION",
    "reason": "MISMATCHED_PAYMENT"
  },
  {
    "name": "wrong bank",
    "ps": [
      {}
    ],
    "credit": {
      "bankId": "B2"
    },
    "out": "EXCEPTION",
    "reason": "MISMATCHED_PAYMENT"
  },
  {
    "name": "wrong merchant",
    "ps": [
      {}
    ],
    "credit": {
      "merchantId": "m2"
    },
    "out": "EXCEPTION",
    "reason": "NO_EXACT_MATCH"
  },
  {
    "name": "wrong reference",
    "ps": [
      {}
    ],
    "credit": {
      "reference": "OTHER"
    },
    "out": "EXCEPTION",
    "reason": "NO_EXACT_MATCH"
  },
  {
    "name": "missing reference",
    "ps": [
      {}
    ],
    "credit": {
      "reference": ""
    },
    "out": "EXCEPTION",
    "reason": "INVALID_EVENT"
  },
  {
    "name": "unauthenticated event",
    "ps": [
      {}
    ],
    "credit": {
      "authenticated": false
    },
    "out": "EXCEPTION",
    "reason": "UNTRUSTED_SOURCE"
  },
  {
    "name": "screenshot level even authenticated",
    "ps": [
      {}
    ],
    "credit": {
      "evidenceLevel": "CUSTOMER_SCREENSHOT"
    },
    "out": "EXCEPTION",
    "reason": "UNTRUSTED_SOURCE"
  },
  {
    "name": "sms level even authenticated",
    "ps": [
      {}
    ],
    "credit": {
      "evidenceLevel": "SMS_NOTIFICATION"
    },
    "out": "EXCEPTION",
    "reason": "UNTRUSTED_SOURCE"
  },
  {
    "name": "authorized delegate",
    "ps": [
      {}
    ],
    "credit": {
      "evidenceLevel": "AUTHORIZED_BANK_DELEGATE"
    },
    "out": "PAID"
  },
  {
    "name": "late credit",
    "ps": [
      {}
    ],
    "credit": {
      "occurredAt": "2026-11-01T00:00:00Z"
    },
    "out": "EXCEPTION",
    "reason": "LATE_PAYMENT"
  },
  {
    "name": "canceled payment",
    "ps": [
      {
        "status": "CANCELED"
      }
    ],
    "credit": {},
    "out": "EXCEPTION",
    "reason": "CANCELED_REQUEST"
  },
  {
    "name": "already paid order",
    "ps": [
      {
        "status": "PAID"
      }
    ],
    "credit": {},
    "out": "EXCEPTION",
    "reason": "ALREADY_PAID"
  },
  {
    "name": "ambiguous two orders",
    "ps": [
      {},
      {
        "paymentId": "p2"
      }
    ],
    "credit": {},
    "out": "EXCEPTION",
    "reason": "AMBIGUOUS_MATCH"
  },
  {
    "name": "similar amount only",
    "ps": [
      {
        "reference": "OTHER"
      }
    ],
    "credit": {},
    "out": "EXCEPTION",
    "reason": "NO_EXACT_MATCH"
  },
  {
    "name": "negative amount",
    "ps": [
      {}
    ],
    "credit": {
      "amountMinor": -1
    },
    "out": "EXCEPTION",
    "reason": "INVALID_EVENT"
  },
  {
    "name": "fractional amount",
    "ps": [
      {}
    ],
    "credit": {
      "amountMinor": 12000.5
    },
    "out": "EXCEPTION",
    "reason": "INVALID_EVENT"
  },
  {
    "name": "invalid currency",
    "ps": [
      {}
    ],
    "credit": {
      "currency": "VN"
    },
    "out": "EXCEPTION",
    "reason": "INVALID_EVENT"
  },
  {
    "name": "invalid timestamp",
    "ps": [
      {}
    ],
    "credit": {
      "occurredAt": "yesterday"
    },
    "out": "EXCEPTION",
    "reason": "INVALID_EVENT"
  },
  {
    "name": "no eligible requests",
    "ps": [],
    "credit": {},
    "out": "EXCEPTION",
    "reason": "NO_EXACT_MATCH"
  },
  {
    "name": "two merchants same reference",
    "ps": [
      {},
      {
        "paymentId": "p2",
        "merchantId": "m2"
      }
    ],
    "credit": {},
    "out": "PAID"
  },
  {
    "name": "two banks same reference",
    "ps": [
      {},
      {
        "paymentId": "p2",
        "bankId": "B2"
      }
    ],
    "credit": {},
    "out": "PAID"
  }
];
for(const c of cases){test(c.name,()=>{const result=reconcile(fresh(c.ps.map(p=>({...baseP,...p}))),{...baseC,...c.credit});assert.equal(result.outcome,c.out);if(c.reason)assert.equal(result.reason,c.reason);assert.equal(result.state.allocations.length,c.out==="PAID"?1:0);});}
test("100 duplicate callbacks are idempotent",()=>{let r=reconcile(fresh([baseP]),baseC);for(let i=0;i<100;i++){r=reconcile(r.state,baseC);assert.equal(r.outcome,"REPLAY");}assert.equal(r.state.events.length,1);assert.equal(r.state.allocations.length,1);assert.equal(r.state.outbox.length,1);});
test("conflicting duplicate id fails closed",()=>{const a=reconcile(fresh([baseP]),baseC);const b=reconcile(a.state,{...baseC,amountMinor:99999});assert.equal(b.reason,"CONFLICTING_DUPLICATE");assert.equal(b.state.allocations.length,1);});
test("second credit cannot allocate already paid order",()=>{const a=reconcile(fresh([baseP]),baseC);const b=reconcile(a.state,{...baseC,bankTransactionId:"TX002"});assert.equal(b.reason,"ALREADY_PAID");assert.equal(b.state.allocations.length,1);});
