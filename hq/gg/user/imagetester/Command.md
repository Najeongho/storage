## qwalk.py를 활용한 Windows SMB 마운트 드라이브 ACL 설정 명령어 (imagetester 사용자, 특정 Role 적용)

> ** 주의:

* 이 스크립트는 Windows OS의 SMB 마운트 드라이브에서 실행되어야 합니다.
* Python 3 및 `qwalk.py` 스크립트가 설치되어 있어야 합니다.
* `imagetester` 사용자가 이미 생성되어 있어야 합니다.
* 스크립트 실행 권한 및 대상 디렉토리 수정 권한이 필요합니다.
* **스크립트 실행 전 반드시 백업을 수행하십시오.** 잘못된 권한 설정은 데이터 손실을 초래할 수 있습니다.

> ** 명령어:

```bash
python qwalk.py Z:\testimagedata --smb --user imageadmin --modify-acl imageadmin:full_control,"BUILTIN\imagetester:(OI)(CI)(RX)"
```

> ** 설명:

1. `python qwalk.py`: `qwalk.py` 스크립트를 Python 인터프리터로 실행합니다.
2. `Z:\testimagedata`: ACL을 설정할 대상 디렉토리 경로입니다. (SMB 마운트 드라이브 Z: 아래의 testimagedata 디렉토리)
3. `--smb`: SMB 프로토콜을 사용하여 파일에 접근하도록 지정합니다.
4. `--user imageadmin`: `imageadmin` 사용자 권한으로 스크립트를 실행합니다. (일반적으로 관리자 권한이 필요)
5. `--modify-acl imageadmin:full_control,"BUILTIN\imagetester:(OI)(CI)(RX)"`: 
    * `imageadmin` 사용자에게는 모든 권한 (`full_control`)을 부여합니다.
    * `imagetester` 사용자에게는 다음 권한을 부여합니다.
        * `(OI)`: Object Inheritance - 하위 객체에 대한 권한 상속 허용
        * `(CI)`: Container Inheritance - 하위 컨테이너(폴더)에 대한 권한 상속 허용
        * `(RX)`: Read and Execute - 읽기 및 실행 권한 부여

> ** 스크립트 동작:

* `qwalk.py` 스크립트는 `Z:\testimagedata` 디렉토리 및 하위 디렉토리, 파일들을 순회합니다.
* 각 항목에 대해 현재 ACL을 확인하고, `imageadmin` 사용자와 `imagetester` 사용자에게 지정된 권한을 부여하는 ACL을 추가합니다.
* 수정된 ACL은 `imageadmin` 사용자 권한으로 적용됩니다.

> ** 추가 참고:

* `qwalk.py` 스크립트의 GitHub 저장소: [https://github.com/Qumulo/qumulo-filesystem-walk](https://github.com/Qumulo/qumulo-filesystem-walk)
* `qwalk.py` 사용법 및 옵션에 대한 자세한 내용은 저장소의 README 파일을 참조하십시오.
* Windows ACL에 대한 자세한 내용은 Microsoft 공식 문서를 참조하십시오.

> ** 주의사항:

* 위 명령어는 `imagetester` 사용자에게 읽기 및 실행 권한만 부여하는 예시입니다. 필요에 따라 권한을 수정해야 합니다.
* `BUILTIN\` 접두사는 로컬 그룹을 나타냅니다. 만약 도메인 그룹을 사용하는 경우, 접두사를 수정해야 합니다. (예: `DOMAIN\imagetester`)
* ACL 설정은 시스템 및 데이터 보안에 큰 영향을 미칠 수 있습니다. 신중하게 진행하고, 반드시 백업을 수행하십시오.