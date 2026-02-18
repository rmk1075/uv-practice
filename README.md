# uv-practice

## Features

### Python

- uv python install [OPTIONS] [TARGETS]

[TARGETS] 으로 지정한 버전의 python 을 설치하는 명령어
[OPTIONS] 로는 reinstall, force, upgrade 등이 있다.

- uv python list [OPTIONS] [REQUEST]

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

- uv python find [OPTIONS] [REQUEST]

현재 project 에서 설치된 파이썬 버전을 출력

- uv python pin [OPTIONS] [REQUEST]

[REQUEST] 로 입력한 버전의 파이썬을 현재 프로젝트에서 사용하도록 고정하는 명령어

pin 명령어를 사용하면 고정된 버전을 입력한 .python-version 파일이 생성된다.
이후 find 명령어를 실행하면 파이썬 버전이 변경된 것을 확인할 수 있다.

- uv python uninstall [OPTIONS] [REQUEST]

[REQUEST] 로 입력한 버전의 파이썬을 삭제하는 명령어
