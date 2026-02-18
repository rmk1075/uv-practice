# uv-practice

## Features

### Python

#### uv python install [OPTIONS] [TARGETS]

[TARGETS] 으로 지정한 버전의 python 을 설치하는 명령어
[OPTIONS] 로는 reinstall, force, upgrade 등이 있다.

#### uv python list [OPTIONS] [REQUEST]

설치 가능한 파이썬 버전을 출력하는 명령어

[REQUEST] 에 조회하고 싶은 버전을 입력하면 아래와 같이 해당 버전의 파이썬만 출력된다.

```shell
$ uv python list 3.13
cpython-3.13.12-linux-aarch64-musl    /usr/local/bin/python3.13
cpython-3.13.12-linux-aarch64-musl    /usr/local/bin/python3 -> python3.13
cpython-3.13.12-linux-aarch64-musl    /usr/local/bin/python -> python3
cpython-3.13.12-linux-aarch64-musl    <download available>
```

따로 버전을 입력하지 않으면 아래와 같이 전체 버전의 파이썬이 출력된다.

```
$ uv python list
cpython-3.15.0a6-linux-aarch64-musl                 <download available>
cpython-3.15.0a6+freethreaded-linux-aarch64-musl    <download available>
cpython-3.14.3-linux-aarch64-musl                   /root/.local/share/uv/python/cpython-3.14-linux-aarch64-musl/bin/python3.14
cpython-3.14.3+freethreaded-linux-aarch64-musl      <download available>
cpython-3.13.12-linux-aarch64-musl                  /usr/local/bin/python3.13
cpython-3.13.12-linux-aarch64-musl                  /usr/local/bin/python3 -> python3.13
cpython-3.13.12-linux-aarch64-musl                  /usr/local/bin/python -> python3
cpython-3.13.12-linux-aarch64-musl                  <download available>
cpython-3.13.12+freethreaded-linux-aarch64-musl     <download available>
cpython-3.12.12-linux-aarch64-musl                  <download available>
cpython-3.11.14-linux-aarch64-musl                  <download available>
cpython-3.10.19-linux-aarch64-musl                  <download available>
cpython-3.9.25-linux-aarch64-musl                   <download available>
```

#### uv python find [OPTIONS] [REQUEST]

현재 project 에서 설치된 파이썬 버전을 출력

#### uv python pin [OPTIONS] [REQUEST]

[REQUEST] 로 입력한 버전의 파이썬을 현재 프로젝트에서 사용하도록 고정하는 명령어

pin 명령어를 사용하면 고정된 버전을 입력한 .python-version 파일이 생성된다.
이후 find 명령어를 실행하면 파이썬 버전이 변경된 것을 확인할 수 있다.

#### uv python uninstall [OPTIONS] [REQUEST]

[REQUEST] 로 입력한 버전의 파이썬을 삭제하는 명령어

### Projects

#### uv init [OPTIONS] [PATH]

지정한 경로 [PATH] 에 새로운 파이썬 프로젝트를 생성하는 명령어
프로젝트 경로 아래에 .python-version, README.md, pyproject.toml, main.py 등의 파일이 생성된다.

새로 생성된 프로젝트에서 처음으로 실행 명령어 (uv run, uv sync, uv lock 등) 을 실행하면 가상환경 .venv 와 uv.lock 파일이 프로젝트 루트에 생성된다.

- pyproject.toml: 프로젝트 메타 데이터를 저장하고 있는 파일. 프로젝트 의존성뿐만 아니라 프로젝트 설명, 라이센스 등의 세부정보를 지정하는데 사용된다. 직접 수정할 수도 있고, uv add 나 uv remove 와 같은 명령어로 관리할 수도 있다.
- .python-version: 프로젝트의 기본 파이썬 버전을 저장한 파일. 프로젝트의 가상환경을 생성할 때 사용할 파이썬 버전을 알려준다.
- .venv: 프로젝트의 파이썬 가상환경
- uv.lock: 프로젝트 의존성 정보를 가지고 있는 크로스 플랫폼 lockfile. 프로젝트의 전반적인 내용이 포함된 pyproject.toml 과 달리 정확하게 프로젝트 환경에 설치된 버전만 포함한다. 수동으로 수정하면 안되고 uv 를 통해서만 관리되야 하며, 버전 관리를 통해서 다른 환경에서도 프로젝트 환경을 재현될 수 있도록 관리해야 한다.

#### uv add [OPTIONS] <PACKAGES|--requirements <REQUIREMENTS>>

파이썬 패키지 의존성을 추가하는 명령어
실행하면 아래와 같이 지정한 패키지와 의존 관계에 있는 패키지들을 설치한다.

```shell
$ uv add requests
Resolved 6 packages in 647ms
Prepared 5 packages in 698ms
░░░░░░░░░░░░░░░░░░░░ [0/5] Installing wheels...                                                                                                                               warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 5 packages in 187ms
 + certifi==2026.1.4
 + charset-normalizer==3.4.4
 + idna==3.11
 + requests==2.32.5
 + urllib3==2.6.3
```

설치가 완료되면 uv.lock 과 pyproject.toml 이 설치된 의존성 정보를 포함하여 업데이트 된다.

#### uv remove [OPTIONS] <PACKAGES>...

프로젝트에 설치된 패키지 의존성을 삭제하는 명령어
명령어를 실행하면 아래와 같이 의존성이 삭제되고 uv.lock 과 pyproject.toml 에서도 관련 정보가 삭제된다.

```shell
$ uv remove requests
Resolved 1 package in 9ms
Uninstalled 5 packages in 80ms
 - certifi==2026.1.4
 - charset-normalizer==3.4.4
 - idna==3.11
 - requests==2.32.5
 - urllib3==2.6.
```

#### uv sync [OPTIONS]

프로젝트 의존성을 동기화시켜 프로젝트 환경을 업데이트 하는 명령어
uv lock 파일 기반으로 의존성을 설치한다.

#### uv lock [OPTIONS]

프로젝트의 lock 파일을 프로젝트 환경에 맞춰 생성한다.
이미 lock 파일이 있는 경우 환경에 맞춰 내용을 업데이트한다.

#### uv run [OPTIONS] [COMMAND]

프로젝트 환경의 명령어나 파이썬 스크립트를 실행한다.
uv run main.py 나 uv run ruff check 등과 같이 파이썬 패키지 명령어를 실행할 수 있다.

#### uv tree [OPTIONS]

프로젝트의 의존성 트리를 출력하는 명령어
실행하면 아래와 같이 패키지 의존성이 트리 형식으로 출력된다.

```shell
$ uv tree
Resolved 6 packages in 5ms
example v0.1.0
└── requests v2.32.5
    ├── certifi v2026.1.4
    ├── charset-normalizer v3.4.4
    ├── idna v3.11
    └── urllib3 v2.6.3
```

#### uv build [OPTIONS] [SRC]

[SRC] 로 지정된 디렉토리의 소스코드를 source distribution (tar.gz) 과 whl 파일로 빌드한다.
[SRC] 경로를 따로 지정하지 않으면 현재 위치를 [SRC] 로 빌드가 진행된다.
빌드된 산출물은 dist 디렉토리 아래에 저장된다.

#### uv publish [OPTIONS] [FILES]...

빌트된 프로젝트 아카이브를 패키지 저장소에 배포하는 명령어
