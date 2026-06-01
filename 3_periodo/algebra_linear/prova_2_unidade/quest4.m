% Questão 04 - Condução não estacionária de calor em uma barra

clc;
C = 1;

A = [1+2*C   -C      0       0;
     -C      1+2*C   -C      0;
      0      -C      1+2*C   -C;
      0       0      -C      1+2*C];

% === LETRA A ===
disp('=== (a)');
disp(' ');
disp('Matriz A (tridiagonal):');
disp(A);

[L, U, P] = lu(A);
disp('Matriz L (bidiagonal inferior):');
disp(round(L * 1e4) / 1e4);
disp('Matriz U (bidiagonal superior):');
disp(round(U * 1e4) / 1e4);
disp('Verificação LU - PA (deve ser zeros):');
disp(round((L*U - P*A) * 1e4) / 1e4);

% === LETRA B ===
disp('B');
disp(' ');

t0 = [10; 15; 15; 10];
fprintf('t0 = [%g, %g, %g, %g]^T\n', t0);
disp(' ');

T = t0;
for k = 1:4
  T = U \ (L \ (P * T));
  fprintf('t%d = [%.4f, %.4f, %.4f, %.4f]^T\n', k, T(1), T(2), T(3), T(4));
end
