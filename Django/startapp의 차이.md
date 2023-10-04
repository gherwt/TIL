## django-admin startapp v/s python prepare.py startapp

django-admin startapp 및 python Manage.py startapp는 모두 프로젝트 내에서 새 Django 앱을 만드는 데 사용되는 명령어이다. 그러나 둘은 다르게 실행됩니다.

django-admin은 새 앱 생성을 포함하여 다양한 Django 관련 작업을 실행할 수 있는 명령어이다. django-admin을 사용하여 새 앱을 만들려면 `터미널`에 다음 명령을 입력하면 된다.

> django-admin startapp <app_name>

반면에 python Manage.py는` 현재 작업 중인 Django 프로젝트와 관련된 명령줄` 도구입니다. 이를 통해 새 앱 생성을 포함하여 다양한 프로젝트 관련 작업을 실행할 수 있습니다. Python Manage.py를 사용하여 새 앱을 만들려면 터미널에 다음 명령을 입력합니다.

> python manage.py startapp <app_name>

두 명령 모두 지정된 이름으로 새 Django 앱을 생성하지만 `python prepare.py startapp 은 Django 프로젝트 내`에서 새 앱을 만드는 데 권장되는 방법입니다. 이를 통해 프로젝트 컨텍스트 내에서 적절한 프로젝트 설정을 사용하여 앱이 생성되도록 보장할 수 있습니다.