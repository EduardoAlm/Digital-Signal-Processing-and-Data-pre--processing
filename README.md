# Digital-Signal-Processing-and-Data-pre--processing

These python scripts consist in some experiments in order to improve my knowledge in signal processing and adaptation of matlab scripts to Python. The data used pertains seismic events.

The Downloader and get-data scripts are finished and make easier getting data from platforms such as IRIS.

The other three scripts (forw, stft and main) are still incomplete for the data has been processed, through the use of the stft algorithm ..., but the data final result visualization is still to be done. These three make use of the obspy framework as well as matplotlib, scipy and numpy libraries.

This repo also contains two more scripts one in matlab and another in python that contain a simple code to approximate continuous periodic functions using the fourier series.
The Fourier series works in a specific domain (whilst the fourier transform goes from -inf to +inf) it's also important to denote the gibbs effect when approximating discontinuous functions using fourier series.

The fourier Transform allows us to "transport" a function into a fourier space in with we can easily compute the derivatives of functions and after we got the solution through the Fourier transform pair we can use the FT inverse to go back to the physical space.

Most times the data we are given comprises in a vector of data from certain sampling points and in order to understand this data we can apply the discrete fourier transform (DFT) which will allow us to 
separate the sampled data into a sum of sines and cosines. This is very useful to identify if its audio data and if it is what are the tones that add up to create that particular audio, you can separate the sounds in a file in order to find variances that shouldn't be there much like some people 
can identify if a car has a problem by identifying a weird noise. This algorithm amongst many other applications its crucial in signal processing. The resulting complex fourier coefficients capture indicate the magnitude and phase of the signal.

The DFTmatrix matlab file has two ways of computing the DFT matrix a slow, and a faster way even thought when computing the DFT you will always use the fast fourier transform (FFT) for its development consists in making the DFT computationally efficient.

When applying the FFT inside the returned vector reside the fourier coefficients. Each of these coefficients will always have a magnitude (which tells us the importance of that specific frequency, how much we have it) and phase (this tells us if this frequency is more sin or cos).

The DenoisingFFT python and matlab scripts employ the FFT in order to efficiently perform the DFT and obtain the fourier coefficients. Through these we can now single out the frequencies we are interested in by defining a threshold and zeroing out the frequencies bellow that very same threshold. After that we can recover our (now filtered) signal by performing an inverse of the fft.
