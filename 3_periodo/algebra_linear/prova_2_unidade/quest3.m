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
    % interpolação linear na borda direita
    if n == 1
      T_right = 7.5;
    else
      T_right = 7 + (i-1)*(8-7)/(n-1);
    end

    for j = 1:m
      k = (i-1)*m + j;  % índice global do ponto
      A(k,k) = 4;

      % vizinho esquerdo
      if j > 1
        A(k, k-1) = -1;
      else
        b(k) = b(k) + T_left;
      end

      % vizinho direito
      if j < m
        A(k, k+1) = -1;
      else
        b(k) = b(k) + T_right;
      end

      % vizinho acima
      if i > 1
        A(k, k-m) = -1;
      else
        b(k) = b(k) + T_top;
      end

      % vizinho abaixo
      if i < n
        A(k, k+m) = -1;
      else
        b(k) = b(k) + T_bot;
      end
    end
  end
end

% === LETRA D ===
disp('=== (d) Função monta_sistema(m, n) implementada ===');
disp('Constrói A (banda pentadiagonal) e b para malha m x n.');
disp(' ');

input('--- Pressione Enter para continuar para (e) ---');

% === LETRA E ===
disp('=== (e) Teste com m=4, n=2 (reproduz problema original) ===');
disp(' ');
[A_test, b_test] = monta_sistema(4, 2);
disp('Matriz A gerada:'); disp(A_test);
disp('Vetor b gerado:'); disp(b_test');

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
  disp('✓ A e b coincidem com o enunciado!');
else
  disp('✗ Divergência encontrada.');
  disp('Diferença em A:'); disp(A_test - A_orig);
  disp('Diferença em b:'); disp(b_test - b_orig);
end

input('--- Pressione Enter para continuar para (f) ---');

% === LETRA F ===
disp('=== (f) Solução e mapa de calor para m=4, n=2 ===');
disp(' ');
[A_f, b_f] = monta_sistema(4, 2);
[L, U, P]  = lu(A_f);
x_f        = U \ (L \ (P * b_f));

disp('Temperaturas nos pontos interiores (matriz n x m):');
T_matrix = reshape(x_f, 4, 2)';
disp(T_matrix);

% Mapa de calor com bordas
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
title('Distribuição de Temperatura na Placa (m=4, n=2)');
xlabel('Posição horizontal');
ylabel('Posição vertical');

input('--- Pressione Enter para continuar para (g) ---');

% === LETRA G ===
disp('=== (g) Estudo de escalabilidade ===');
disp(' ');
sizes = [10 20 50 100];  % removido 200 para não travar

fprintf('%-12s %-12s %-12s %-12s %-14s\n', ...
        'Malha', 'T_montar(s)', 'T_fatorar(s)', 'T_resolver(s)', 'T_inversa(s)');

for s = sizes
  m = s; n = s; N = m*n;

  t1 = tic;
  [A_g, b_g] = monta_sistema(m, n);
  A_sp = sparse(A_g);  % já converte para sparse
  t_build = toc(t1);

  t2 = tic;
  [L_g, U_g, P_g] = lu(A_sp);  % LU esparsa
  t_lu = toc(t2);

  t3 = tic;
  U_g \ (L_g \ (P_g * b_g));
  t_solve = toc(t3);

  if N <= 400  % só calcula inversa para malhas pequenas
    t4 = tic;
    inv(full(A_sp));
    t_inv = toc(t4);
    str_inv = sprintf('%.4f', t_inv);
  else
    str_inv = 'N/A (muito grande)';
  end

  fprintf('%-12s %-12.4f %-12.4f %-12.4f %-20s\n', ...
          sprintf('%dx%d',m,n), t_build, t_lu, t_solve, str_inv);
end

disp(' ');
disp('Conclusão: fatoração LU esparsa é muito mais rápida e econômica');
disp('em memória do que calcular A^{-1} para matrizes grandes.');

input('--- Pressione Enter para continuar para (h) ---');

% === LETRA H ===
disp('=== (h) Esparsidade para malha 100x100 ===');
disp(' ');
[A_h, b_h] = monta_sistema(100, 100);
N_h        = 100*100;
nnz_dense  = nnz(A_h);
total      = N_h^2;
pct        = 100 * nnz_dense / total;

fprintf('Elementos não nulos: %d de %d (%.4f%%)\n', nnz_dense, total, pct);
disp(' ');

% Versão esparsa
A_sparse = sparse(A_h);

t_dense_lu = tic;
lu(A_h);
t_dense_lu = toc(t_dense_lu);

t_sparse_lu = tic;
lu(A_sparse);
t_sparse_lu = toc(t_sparse_lu);

fprintf('Tempo LU densa:  %.4f s\n', t_dense_lu);
fprintf('Tempo LU esparsa: %.4f s\n', t_sparse_lu);
disp(' ');
disp('Conclusão: matriz esparsa usa muito menos memória e é');
disp('significativamente mais rápida para fatoração LU.');