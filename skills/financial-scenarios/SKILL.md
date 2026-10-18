---
name: financial-scenarios
description: "Translate a business decision into an auditable range-based commercial and financial model. Use when: Commercial viability, resource allocation, investment, operating strategy, pricing, runway or build-buy-partner tradeoffs need numerical consideration."
---
# Financial Scenarios

**Purpose:** Translate a business decision into an auditable range-based commercial and financial model.

## When to use

Commercial viability, resource allocation, investment, operating strategy, pricing, runway or build-buy-partner tradeoffs need numerical consideration.

## Inputs

Revenue mechanisms, costs, volume/unit definitions, time horizon, capital assumptions, constraints, actuals provenance, baseline and decision thresholds.

## Method

1. Define economic unit, cohort, time basis, currency, tax and inflation assumptions before applying formulas.
2. Separate reported actuals, benchmark-based assumptions, management guesses and analyst estimates in an assumptions register.
3. Link price, reach, conversion, churn/retention, variable costs, fixed capacity, working capital and financing terms appropriately.
4. Construct base, downside, upside and explicit failure cases rather than one falsely precise forecast.
5. Run sensitivity, breakeven, liquidity/runway and capital/dilution analyses as relevant.
6. Report viability conditions, what evidence would most improve a decision and which estimates are non-decision-grade.

## Outputs

Assumption dictionary; scenario model design; sensitivity matrix; business unit economics; runway/capital requirements; uncertainties memo.

## Quality gates

- Every figure has units, currency, period and provenance.
- Numerical models are not validated merely because formulas calculate.
- Escalate tax, legal, accounting or investment conclusions for qualified review.
- No invented comparable data or precise valuations.
- Prefer evidence-linked, economical work proportionate to actual decision risk.

## Handoff contract

State engagement ID, bounded objective, source and claim IDs, open assumptions, options, reviewer, approval owner, and next test.

## Evaluation

Use `evals/financial-scenarios.json` with representative, ambiguous, and adversarial cases against a no-skill baseline. Structural checks alone are not effectiveness proof.
