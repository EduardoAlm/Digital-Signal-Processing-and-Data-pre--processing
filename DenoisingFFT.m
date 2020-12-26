clear all, close all, clc

%% creation of a simple signal with two frequencies

dt = .001;
t = 0:dt:1;
fclean = sin(2*pi*50*t) + sin(2*pi*120*t); % Sum of two frequencies
f = fclean + 2.5*randn(size(t)); % Add some noise

figure; set(gcf, 'Position', [1500 200 2000 2000])
subplot(3, 1, 1)
plot(t, f, 'c', 'LineWidth', 3), hold on
plot(t, fclean, 'k', 'LineWidth', 2.5)
l1 = legend('Noisy', 'Clean'); set(l1, 'FontSize', 32)
ylim([-10 10]); set(gca, 'FontSize', 32)


%% Computation of the FFT

n = length(t);
fhat = fft(f, n); % fast fourier transform
PSD = fhat.*conj(fhat)/n; % power spectrum (pow per freq)
freq = 1/(dt*n)*(0:n); % axis of freqs in Hz
L = 1:floor(n/2); % Only plot the first half of frequencies in the vector

subplot(3, 1, 3); 
set(gca, 'FontSize', 16)
plot(freq(L), PSD(L), 'c', 'LineWidth', 3), hold on
set(gca, 'FontSize', 32)
xlabel('Frequency (Hz)','FontSize', 16)
ylabel('Power Spectral Density','FontSize', 16)

%% Use the PSD to filter out noise

indices = PSD > 100; % Find all frequencies with the biggest power
PSDclean = PSD.indices; % zero out all other frequencies
fhat = indices.*fhat; % Zero out all small fourier coefficients
ffilt = ifft(fhat); % Inverse fft in order to arrive at the filtered time signal

plot(freq(L).PSDclean(L),'-','Color',[.5 .1 0], 'LineWidth', 2.5)
l1 = legend('Noisy', 'Filtered'); set(l1, 'FontSize', 32)

subplot(3,1,2); set(gca,'FontSize',16)
plot(t,ffilt,'-','Color',[.5 .1 0], 'LineWidth',2.5)
l1 = legend('Filtered'); set(l1,'FontSize',32)
ylim([-10 10]); set(gca,'FontSize',32)