# ckanext-odao

오픈마켓 웹서비스에서 ID/Password 기반 사용자 인증 시 CKAN의 사용자 정보를 기반으로 인증을 수행하기 위한 extension

## 디렉토리 구조 
```
ckanext-odao
│   README.md   // this file
│
│   setup.cfg, setup.py     //  설치 관련 파일 (플러그인 개발 도구에서 자동 생성)
│   
│   MANIFEST.in         //  Extension에 포함된 파일 목록 
│
│   requirements.txt, dev-requirements.txt    //  종속 라이브러리 설치용 목록 
│
└───ckanext
    └───odao
        │   plugin.py   //  plugin 메인 로직 
```

## 설치 
```
cd /home/ubuntu/ckan/lib/default/src/
git clone https://github.com/thyun4synctechno/ckanext-odao.git

cd ckanext-odao
pip install -e .
pip install -r requirements.txt
```


--- 
## 이하 내용은 샘플로 자동생성된 설명이므로 참고

## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | not tested    |

Suggested values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-odao:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    cd /usr/lib/ckan/default/src/
    git clone https://github.com//ckanext-odao.git
    cd ckanext-odao
    pip install -e .
	pip install -r requirements.txt

3. Add `odao` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.odao.some_setting = some_default_value


## Developer installation

To install ckanext-odao for development, activate your CKAN virtualenv and
do:

    git clone https://github.com//ckanext-odao.git
    cd ckanext-odao
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-odao

If ckanext-odao should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
