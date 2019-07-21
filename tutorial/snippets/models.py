from django.db import models

# pygments: Code Styling Tool
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# pygments end

# lexers
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# lexers end

class Snippet(models.Model):
    # 언제 생성되었는지
    created = models.DateTimeField(auto_now_add=True)
    # 제목
    title = models.CharField(max_length = 100, blank = True, default = '')
    # 코드
    code = models.TextField()
    # linenos (코드 라인 표시 줄 표현 x이면 false, 표현 o이면 true)
    linenos = models.BooleanField(default=False)
    # language (어떤 언어를 기준으로 코드 highlight 할 것인지)
    language = models.CharField(choices=LANGUAGE_CHOICES, default = 'python', max_length = 100)
    # style
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)

    class Meta:
        ordering = ['created'] # 생성된 날짜를 기준으로 객체들을 정렬, 역순은 -created
    
    def __str__(self):
        return self.title