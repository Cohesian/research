# Findings and Limitations

## Finding supported by this study

Within the declared finite system, changing only the symmetric type-affinity
matrix changed the distribution of measured structures. Relative to uniform
attraction, selective affinity increased:

- the mean maximum connected fraction under both initialization methods;
- the late-run mean contact degree under random initialization; and
- the magnitude of negative tail potential energy.

The blue-noise/selective peak was consistent across the three seeds
($0.153\pm0.006$), while random/selective was variable
($0.160\pm0.063$). Initialization therefore affected reproducibility even when
the condition means were similar.

This is an example of emergence in the operational sense used by the study:
a local pair rule changed higher-scale graph observables and visible connected
morphology, although no global structure was prescribed.

The strongest statement supported by the current data is therefore:

> In this finite, thermostatted patchy-particle model, changing the local
> type-affinity matrix changed the sampled distribution of connected
> structures while all other declared study parameters were held fixed.

The experiment does not support the stronger statement that selective affinity
always produces larger structures. The random/selective sample has substantial
seed variance, and the ensemble is small.

## What the study does not establish

The ensemble does not yet establish:

- a stable thermodynamic phase;
- a phase transition or critical point;
- a universal scaling exponent;
- persistence in the infinite-time limit;
- behavior in the infinite-system limit; or
- an atomistic interpretation.

The largest components remained finite and fluctuating. Three seeds are enough
to reveal obvious seed sensitivity, but not enough for a strong distributional
claim.

## Next controlled extensions

A later study should extend one axis at a time:

1. increase the number of seeds;
2. compare multiple particle counts at fixed number density;
3. lengthen the simulated duration;
4. halve $\Delta t$ to test numerical convergence;
5. sweep thermal energy or selected affinity coefficients; and
6. quantify cluster lifetime, branching, cycles, and type composition.

Rigid bodies are unnecessary for the current model. A rigid body would encode
a predeclared multi-bead geometry; applying it to discovered clusters would
freeze the very assembly process under observation. Dynamic patch creation and
field-mediated interactions remain separate future questions until this
fixed-patch baseline is better characterized.
