% questao01.m
M = [0.299  0.587  0.114;
     0.596 -0.275 -0.321;
     0.212 -0.528  0.311];

M_inv = inv(M);

fprintf('Matriz inversa (converte YIQ -> RGB):\n');
disp(M_inv);

fprintf('\nEquação de conversão:\n');
fprintf('R = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(1,:));
fprintf('G = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(2,:));
fprintf('B = %.4f*Y + %.4f*I + %.4f*Q\n', M_inv(3,:));

% Verificação: M_inv * M deve ser identidade
fprintf('\nVerificação M^{-1} * M (deve ser identidade):\n');
disp(M_inv * M);

%

% questao02.m
A = [ 4 -1 -1  0  0  0  0  0;
     -1  4  0 -1  0  0  0  0;
     -1  0  4 -1 -1  0  0  0;
      0 -1 -1  4  0 -1  0  0;
      0  0 -1  0  4 -1 -1  0;
      0  0  0 -1 -1  4  0 -1;
      0  0  0  0 -1  0  4 -1;
      0  0  0  0  0 -1 -1  4];

b = [5; 15; 0; 10; 0; 10; 20; 30];

% (a) Fatoração LU
[L, U, P] = lu(A);
fprintf('=== (a) Fatoração LU ===\n');
fprintf('Matriz L:\n'); disp(L);
fprintf('Matriz U:\n'); disp(U);
fprintf('Verificação LU - PA (deve ser zeros):\n');
disp(L*U - P*A);

% (b) Resolver Ax = b via LU
% PA x = Pb => L y = Pb, depois U x = y
Pb = P * b;
y  = L \ Pb;
x  = U \ y;
fprintf('=== (b) Solução x = Ax=b ===\n');
disp(x);

% Verificação
fprintf('Verificação A*x - b (deve ser zeros):\n');
disp(A*x - b);

% (c) Inversa de A
A_inv = inv(A);
fprintf('=== (c) Inversa de A ===\n');
disp(A_inv);
fprintf('Nota: A^{-1} é densa, sem estrutura de banda.\n');