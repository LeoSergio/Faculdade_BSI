clc;
M = [0.299  0.587  0.114;
     0.596 -0.275 -0.321;
     0.212 -0.528  0.311];

M_inv = inv(M);

disp(' ');

disp(M_inv);

disp('Equação de conversão:');
fprintf('R = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(1,:));
fprintf('G = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(2,:));
fprintf('B = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(3,:));
disp(' ');

disp(round(M_inv * M * 1e4) / 1e4);