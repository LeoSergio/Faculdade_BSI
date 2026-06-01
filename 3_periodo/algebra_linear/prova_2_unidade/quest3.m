% Questão 03 - Generalização para malha m x n
clc;

function [A, b] = monta_sistema(m, n)
  N = m * n;
  A = zeros(N, N);
  b = zeros(N, 1);

  T_top   = 0;
  T_bot   = 10;
  T_left  = 5;

  for i = 1:n
    if n == 1
      T_right = 7.5;
    else
      T_right = 7 + (i-1)*(8-7)/(n-1);
    end

    for j = 1:m
      k = (i-1)*m + j;
      A(k,k) = 4;

      if j > 1
        A(k, k-1) = -1;
      else
        b(k) = b(k) + T_left;
      end

      if j < m
        A(k, k+1) = -1;
      else
        b(k) = b(k) + T_right;
      end

      if i > 1
        A(k, k-m) = -1;
      else
        b(k) = b(k) + T_top;
      end

      if i < n
        A(k, k+m) = -1;
      else
        b(k) = b(k) + T_bot;
      end
    end
  end
end

% === LETRA D ===
disp('=== (d) ===');
disp('Função monta_sistema(m, n) implementada.');
disp(' ');


% === LETRA E ===
disp('=== (e) ===');
disp(' ');
[A_test, b_test] = monta_sistema(4, 2);
disp('Matriz A:'); disp(A_test);
disp('Vetor b:'); disp(b_test');

A_orig = [ 4 -1 -1  0  0  0  0  0;
          -1  4  0 -1  0  0  0  0;
          -1  0  4 -1 -1  0  0  0;
           0 -1 -1  4  0 -1  0  0;
           0  0 -1  0  4 -1 -1  0;
           0  0  0 -1 -1  4  0 -1;
           0  0  0  0 -1  0  4 -1;
           0  0  0  0  0 -1 -1  4];
b_orig = [5; 15; 0; 10; 0; 10; 20; 30];

if isequal(A_test, A_orig) && isequal(b_test, b_orig)
  disp('A e b coincidem com o enunciado.');
else
  disp('Diferença em A:'); disp(A_test - A_orig);
  disp('Diferença em b:'); disp(b_test - b_orig);
end


% === LETRA F ===
disp('=== (f) ===');
disp(' ');
[A_f, b_f] = monta_sistema(4, 2);
[L, U, P]  = lu(A_f);
x_f        = U \ (L \ (P * b_f));

disp('Temperaturas (matriz n x m):');
T_matrix = reshape(x_f, 4, 2)';
disp(T_matrix);

T_full = zeros(4, 6);
T_full(1,:)   = 0;
T_full(4,:)   = 10;
T_full(:,1)   = 5;
T_full(2,6)   = 7; T_full(3,6) = 8;
T_full(2,2:5) = T_matrix(1,:);
T_full(3,2:5) = T_matrix(2,:);

figure;
imagesc(T_full);
colorbar;
colormap(hot);
title('Temperatura na Placa (m=4, n=2)');
xlabel('Horizontal');
ylabel('Vertical');





% === LETRA G ===
disp('=== (g) ===');
disp(' ');
sizes = [10 20 50 100];

fprintf('%-12s %-12s %-12s %-12s %-20s\n', ...
        'Malha', 'T_montar(s)', 'T_fatorar(s)', 'T_resolver(s)', 'T_inversa(s)');

for s = sizes
  m = s; n = s; N = m*n;

  t1 = tic;
  [A_g, b_g] = monta_sistema(m, n);
  A_sp = sparse(A_g);
  t_build = toc(t1);

  t2 = tic;
  [L_g, U_g, P_g, Q_g] = lu(A_sp);  % 4 saídas: corrige o warning
  t_lu = toc(t2);

  t3 = tic;
  x_g = Q_g * (U_g \ (L_g \ (P_g * b_g)));  % usa Q na solução
  t_solve = toc(t3);

  if N <= 400
    t4 = tic;
    inv(full(A_sp));
    t_inv = toc(t4);
    str_inv = sprintf('%.4f', t_inv);
  else
    str_inv = 'N/A';
  end

  fprintf('%-12s %-12.4f %-12.4f %-12.4f %-20s\n', ...
          sprintf('%dx%d',m,n), t_build, t_lu, t_solve, str_inv);
end


input('');

% === LETRA H ===
disp('=== (h) ===');
disp(' ');
[A_h, b_h] = monta_sistema(100, 100);
N_h       = 100*100;
nnz_dense = nnz(A_h);
total     = N_h^2;
pct       = 100 * nnz_dense / total;

fprintf('Nao nulos: %d de %d (%.4f%%)\n', nnz_dense, total, pct);
disp(' ');

A_sparse = sparse(A_h);

t_dense_lu = tic;
lu(A_h);
t_dense_lu = toc(t_dense_lu);

t_sparse_lu = tic;
[L_h, U_h, P_h, Q_h] = lu(A_sparse);  % 4 saídas: corrige o warning
t_sparse_lu = toc(t_sparse_lu);

fprintf('LU densa:   %.4f s\n', t_dense_lu);
fprintf('LU esparsa: %.4f s\n', t_sparse_lu);