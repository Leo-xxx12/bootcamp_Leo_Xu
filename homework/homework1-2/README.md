# Homework 1 — Is EMA a “Perfect” Trading Signal for NVIDIA (NVDA)?
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Evaluate whether simple Exponential Moving Average (EMA) rules can, by 
themselves, generate a robust trading strategy for NVDA that beats 
buy-and-hold on a risk-adjusted basis after realistic costs.

## Stakeholder & User
Individual/quant learner executing systematic rules on NVDA; needs an 
evidence-based go/no-go decision for an EMA-only strategy.

<Who decides? Who uses the output? Timing & workflow context>
- Decision owner: same user.
- Users of output: the trader and future reviewers.
- Timing/workflow: EOD signals; trade next open (base) or next close 
(alt).

## Useful Answer & Decision
Judge by Sharpe, Sortino, Max Drawdown, CAGR, turnover, and 4–12 bps 
round-trip costs. Deliver a notebook + memo with best EMA rule (if any), 
stability heatmap, and trades/PNL CSVs. Decision: adopt if it meets the 
success bar; otherwise reject EMA-only.

## Assumptions & Constraints
Daily adjusted OHLCV for NVDA (2010–present), long/flat only, next-open 
fills, no look-ahead, vectorized backtests on local machine.

## Known Unknowns / Risks
Regime shifts; parameter overfit; start-date sensitivity; single-name 
bias.

## Lifecycle Mapping
- Stage 01: This README.
- Stage 02: Collect/validate data.
- Stage 03: Backtest EMA grids.
- Stage 04: Robustness checks (costs/start dates).
- Stage 05: Memo with decision in `/docs/`.

## Repo Plan (for this homework)
`/data`, `/src`, `/notebooks`, `/docs`, `/results` under 
`homework/homework1/`.

