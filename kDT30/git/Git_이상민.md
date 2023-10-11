## Git

코드를 관리하는 도구(버전을 통해)
- 코드 관리도구
- 코드 협업도구
- 코드 배포도구

## Git 명령어

`git [명령어]`

### (1) `git init`

git으로 코드 관리를 시작

- 코드 관리 단위(기준): 폴더
- `(master)` : ~~현재 브랜치명~~
- `.git` 폴더 생성: Git이 관리와 관련된 파일

### (2) `git status`

현재 상태를 출력(Git에게 현재 상태를 물어봄)

- `git init` 직후,
   
  ```
  on branch master
  -> master 라는 브랜치 위에 있어요.

  No commits yet 
  -> 아직 commit이 없어요.

  nothing to commit(creat/copy files and use "git add" to track)
  -> comit할 것이 없어요. (설명충)
  ```

- `test.txt` 파일 생성 후,

   ```
   Untracked files:
   (use "git add <file>..." to include in what will be committed)
         test.txt
 
    -> 추적되지 않은 파일이 있어요.
       (파일명)
   nothing added to commit but untracked files present (use "git add" to track)
   -> commit 하기 위해 add된 것이 없어요. 그러나 추적되지 파일은 있어요.
   ```

- `git add test.txt` 이후,
  
  ```
  On branch master
  Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test.txt
  -> commit할 변경들이 있어요.
  ```


- `git commit` 이후,

  ```
  nothing to commit, working tree clean
  -> commit 할 게 없어요. 작업 폴더는 깔끔해요.
  ```

#### `code .` 을 통해 code 를 열기

- `$ code .` 로 열고 파일에 들어간 후 파일을 수정


- 파일 수정 후,
  
  ```
  On branch main
  Changes not staged for commit:
  -> commit하기 위해 stage 되지 않은 변경 사항이 있어요.

    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   test.txt

  no changes added to commit (use "git add" and/or "git commit -a")
  ```

### (3) `git add [파일명]`

commit을 위한 stage
- `git add . `: 현재 폴더의 모든 변경 사항 stage


### (4) `git commit -m "커밋 메시지"`
> commit == 버전을 생성 == 현재 상태의 스냅샷 촬영

- 처음으로 commit을 할 경우,
  
  ```
  Author identity unknown
  -> 작자 미상
  *** Please tell me who you are.

  Run
  -> 아래의 명령어를 실행해주세요.
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name" 
  ```


- `git config` 설정 후 (`vim` 에디터 창),
  
  ```
  # Please enter the commit message for your changes.
  -> 변경사항에 대한 commit message를 입력해주세요.

  # Lines starting with '#' will be ignored, and an empty message aborts the
  commit.
  -> #로 시작하는 라인은 무시됩니다. 아무것도 없는 메시지는 종료됩니다.
  
  # On branch master
  #
  # Initial commit
  #
  # Changes to be committed:
  #       new file:   test.txt
  ```

### (5) `git config`

Git에 관한 설정

- `git config --global user.email "you@example.com"`: global(전역으로) user의 email을 설정
- `git config --global user.email` : 설정값 확인

### (6) `git log`

현재까지의 commit을 출력

- `git log` 출력화면

  ```
  commit b38f77851013240a17737bf1841b86887a5c9abe
  Author: Lee Sang Min <gherwt46@gmail.com>
  -> 작성자
  Date:   Tue Sep 19 16:24:14 2023 +0900
  -> 날짜

    First commit
    -> 커밋 메시지
  ```

- `git log --oneline`: 한 줄로 출력

 ```
 1082053 (HEAD -> main) Add title
 b38f778 First commit
 ```

### (7) `git remote`

- `git remote add [저장소이름] [저장소주소]`: git remote add origin https://github.com/hkeryfonttlxisdrlw/basic_git

  - git 에게 원격저장소(remote) 추가 (add)를 명령
- 저장소 이름: origin
- 저장소 주소: https://github.com/hkeryfonttlxisdrlw/basic_git 