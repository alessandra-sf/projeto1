print("Ola") 
print("Tudo bem")

"""
douglas@douglas-Inspiron-3584:~/Documentos$ mkdir github-exemplos
douglas@douglas-Inspiron-3584:~/Documentos$ cd github-exemplos/
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos$ git clone git@github.com:alessandra-sf/projeto1.git
Cloning into 'projeto1'...
warning: You appear to have cloned an empty repository.
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos$ git branch
fatal: not a git repository (or any of the parent directories): .git
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos$ ls
projeto1
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos$ cd projeto1/
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ ls
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ ls -a
.  ..  .git
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch -M main
error: refname refs/heads/master not found
fatal: Branch rename failed
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git checkout -b main
Switched to a new branch 'main'
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch -M main
error: refname refs/heads/main not found
fatal: Branch rename failed
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ ls
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ code .
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main

No commits yet

Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	teste.py

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main

No commits yet

Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	teste.py

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git add .
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main

No commits yet

Mudanças a serem submetidas:
  (utilize "git rm --cached <arquivo>..." para não apresentar)
	new file:   teste.py

douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git commit -m "Primeiro commit"
[main (root-commit) 95fef85] Primeiro commit
 1 file changed, 1 insertion(+)
 create mode 100644 teste.py
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main
nothing to commit, working tree clean
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch -M main
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
* main
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main
nothing to commit, working tree clean
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 229 bytes | 22.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:alessandra-sf/projeto1.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git push
Everything up-to-date
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ ls -a
.  ..  .git  teste.py
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (utilize "git add <arquivo>..." para atualizar o que será submetido)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   teste.py

nenhuma modificação adicionada à submissão (utilize "git add" e/ou "git commit -a")
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git add .
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git commit -m "Arquivo modificado"
[main 16fb8c3] Arquivo modificado
 1 file changed, 2 insertions(+), 1 deletion(-)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
* main
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git checkout -b tarefa1
Switched to a new branch 'tarefa1'
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
  main
* tarefa1
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git status
No ramo tarefa1
Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	novo.py

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git add .
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git commit -m "Novo"
[tarefa1 2adf94a] Novo
 1 file changed, 1 insertion(+)
 create mode 100644 novo.py
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git push -u origin tarefa1 
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 535 bytes | 535.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'tarefa1' on GitHub by visiting:
remote:      https://github.com/alessandra-sf/projeto1/pull/new/tarefa1
remote: 
To github.com:alessandra-sf/projeto1.git
 * [new branch]      tarefa1 -> tarefa1
Branch 'tarefa1' set up to track remote branch 'tarefa1' from 'origin'.
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git checkout main
Switched to branch 'main'
Seu ramo está à frente de 'origin/main' por 1 submissão.
  (use "git push" to publish your local commits)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git checkout tarefa1 
Switched to branch 'tarefa1'
Your branch is up to date with 'origin/tarefa1'.
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git checkout -b feature/month-user
Switched to a new branch 'feature/month-user'
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
* feature/month-user
  main
  tarefa1
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git add .
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git commit -m "feat: adding feature/month-user"
[feature/month-user 5c502a1] feat: adding feature/month-user
 1 file changed, 3 insertions(+), 1 deletion(-)
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git push -u origin feature/month-user 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'feature/month-user' on GitHub by visiting:
remote:      https://github.com/alessandra-sf/projeto1/pull/new/feature/month-user
remote: 
To github.com:alessandra-sf/projeto1.git
 * [new branch]      feature/month-user -> feature/month-user
Branch 'feature/month-user' set up to track remote branch 'feature/month-user' from 'origin'.
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ git branch
* feature/month-user
  main
  tarefa1
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos/projeto1$ cd ..
douglas@douglas-Inspiron-3584:~/Documentos/github-exemplos$ cd ..
douglas@douglas-Inspiron-3584:~/Documentos$ mkdir exemplos2
douglas@douglas-Inspiron-3584:~/Documentos$ cd exemplos2/
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2$ git clone git@github.com:alessandra-sf/projeto1.git
Cloning into 'projeto1'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 12 (delta 0), reused 12 (delta 0), pack-reused 0
Receiving objects: 100% (12/12), done.
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2$ cd projeto1/
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ ls
teste.py
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ git branch
* main
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ git branch -M feature/month-user
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ git branch
* feature/month-user
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ code .
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ git pull origin feature/month-user 
From github.com:alessandra-sf/projeto1
 * branch            feature/month-user -> FETCH_HEAD
Updating 95fef85..5c502a1
Fast-forward
 novo.py  | 3 +++
 teste.py | 3 ++-
 2 files changed, 5 insertions(+), 1 deletion(-)
 create mode 100644 novo.py
douglas@douglas-Inspiron-3584:~/Documentos/exemplos2/projeto1$ 

"""