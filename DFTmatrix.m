clear all, close all, clc
n = 1024;
w = exp(-i*2*pi/n);

% The slowlier way of computing the DFT matrix
% for i=1:n
%     for j=1:n
%         DFT[i,j]= w^((i-1)*(j-1));
%     end
% end

% The faster way of solving it 

[I,J] = meshgrid(1:n, 1:n);
DFT = w.^((I-1).*(J-1));
imagesc(real(DFT));
