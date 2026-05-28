
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