clear all, close all, clc

figure 
set(gcf, 'Position', [1500 200 2000 1200])

%definition of the domain
L = pi;
N = 1024;
dx = 2*L/(N-1);
x = -L:dx:L;

%definition of the function (in this case im defining a hat funtion)
f = 0*x;
f(N/4:N/2) = 4*(1:N/4+1)/N; %positive slope
f(N/2+1:3*N/4) = 1-4*(0:N/4-1)/N; %negative slope
plot(x,f,'-k','LineWidth',3.5), hold on

%%Computation of the fourier series (this is an aproximation for the limit has been set to 20 iterations)
CC = jet(20);
A0 = sum(f.*ones(size(x)))*dx/pi; 
fFS = A0/2;
for k=1:20
  A(k) = sum(f.*cos(pi*k*x/L))*dx/pi; %Inner Product a(k)
  B(k) = sum(f.*sin(pi*k*x/L))*dx/pi; %Inner Product b(k)
  fFS = fFS + A(k)*cos(k*pi*x/L) + B(k)*sin(k*x*pi/L);
  plot(x,fFS,'-','Color',CC(k,:),'LineWidth',2);
  pause(.1);
endfor

%%Amplitudes and reconstruction error rate
figure; set(gcf, 'Position', [1500 200 2000 1200])
clear ERR
clear A
fFS = A0/2;
A(1) = A0/2/pi;
ERR(1) = norm(f-fFS);
kmax = 100;
for k=1:kmax
  A(k+1) = sum(f.*cos(pi*k*x/L))*dx/pi; %Inner Product a(k)
  B(k+1) = sum(f.*sin(pi*k*x/L))*dx/pi; %Inner Product b(k)
  fFS = fFS + A(k+1)*cos(k*pi*x/L) + B(k+1)*sin(k*x*pi/L);
  ERR(k+1) = norm(f-fFS)/norm(f);
endfor
thresh = median(ERR)*sqrt(kmax)*4/sqrt(3);
r = max(find(ERR>thresh));
r = 7;
subplot(2,1,1);
semilogy(0:1:kmax,A,'k','LineWidth',1.5);
hold on
semilogy(r,A(r+1),'co','LineWidth',15,'MarkerFaceColor','c');
xlim([0 kmax])
ylim([10^(-7) 1])
ylabel('Mode Amplitude','FontSize', 16)
subplot(2,1,2)
semilogy(0:1:kmax,ERR,'k','LineWidth',1.5)
hold on
semilogy(r,ERR(r+1),'co','LineWidth',15,'MarkerFaceColor','c')
xlabel('Mode Number, k','FontSize', 16)
xlabel('Reconstruction Error','FontSize', 16)
