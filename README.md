# Derivative Experiment

A small experiment that approximates derivatives using finite differences.

## Method

For most functions:

```text
f'(x) ≈ (f(x + Δx) - f(x)) / Δx
```

For exponential expressions (e.g. `2**x`), I experimented with:

```text
f'(x) ≈ (f(x) · f(Δx) - f(x)) / Δx
```

where

```text
Δx = 1e-6
```

Not infinitesimal... Python politely refused to store one.

## Purpose

The goal of this project is to better understand numerical differentiation by implementing it from scratch rather than relying on existing libraries. It is an experiment for learning, not a complete symbolic differentiation engine.

## Usage

```python
derivative(2, operation="x**2 - 2*x")
```

You can also try:

```python
derivative(3, operation="x**3")
derivative(1, operation="2**x")
```
