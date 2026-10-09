# Low precision and honest error

Measurements rarely justify six decimal places. Float16 may already be more precise than the input. Extra precision can still help with multiplication, accumulation, and trigonometry.

Error has causes. A meter reading is not a typing mistake. A reversed sensor is not Gaussian noise. Tolerance and angle errors can have very different effects.

Keep the causes separate. Carry symbolic ε terms until a bound or transformation justifies combining them. Use interval arithmetic when the bounds are known.

Then compare symbolic bounds, interval bounds, and a higher-precision calculation. Watch for cancellation, sign changes, branch changes, quantization, and geometric amplification.

[Statistics and error propagation](statistics-econometrics-and-error-propagation.md) · [Idriç interval experiments](https://github.com/dilapidated-shed/intervals.idr)
