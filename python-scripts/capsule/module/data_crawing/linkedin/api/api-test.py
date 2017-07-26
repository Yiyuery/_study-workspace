# coding='utf-8'
# author:Yiyuery
# TODO: 利用linkedInAPI 爬取数据
from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI

access_token = 'AQVJAwZ2nNiVapiLX5yCQucZQl3Qm21Xc7MOGheqdWvcHacfkFAZcDuHgjX-qevMENwQsNtTgM4WxTpG69zuMLHavA_1skwicCGIcX25URW8Cp1Mv08_zBw5EaqyT6K8NnjmDgZ8nfFII7ieH2DQxFe9yZbrwyo8YgYO9y8fi12-wDBQxq4'

# 获取 access token
def getAccessToken():
    tipFlag = input('Do you have Access Token?(Y/N) ')
    if tipFlag == 'Y' or tipFlag == 'y':
        access_token = input('Insert Access Token: ')
    else:
        access_token = 'AQVJAwZ2nNiVapiLX5yCQucZQl3Qm21Xc7MOGheqdWvcHacfkFAZcDuHgjX-qevMENwQsNtTgM4WxTpG69zuMLHavA_1skwicCGIcX25URW8Cp1Mv08_zBw5EaqyT6K8NnjmDgZ8nfFII7ieH2DQxFe9yZbrwyo8YgYO9y8fi12-wDBQxq4'

def spaces(n):
    print('\n' * n)

def get_content():
    comment = input('Insert text: ')
    title = input('Insert title: ')
    description = input('Insert description: ')
    site = input('Insert URL site: ')
    image = input('Insert URL image: ')

    return comment, title, description, site, image


def get_basic_profile():
    linkedin = PyLinkedinAPI(access_token)
    profile = linkedin.get_basic_profile()
    spaces(1)
    print(profile)


def get_companies():
    linkedin = PyLinkedinAPI(access_token)
    companies = linkedin.get_companies()
    spaces(1)
    print(companies)


def get_profile():
    linkedin = PyLinkedinAPI(access_token)
    fields = input(
        'Enter fields separated by commas without spaces \nEx: id,email-address,... : ')
    companies = linkedin.get_profile(fields.split(','))
    spaces(1)
    print(companies)


def publish_text_on_profile():
    linkedin = PyLinkedinAPI(access_token)
    comment = input('Enter text: ')
    data = linkedin.publish_profile_comment(comment)
    spaces(1)
    print(data)


def publish_text_on_company():
    linkedin = PyLinkedinAPI(access_token)
    id = int(input('Enter id(integer) company: '))
    comment = input('Enter text: ')
    data = linkedin.publish_company_comment(id, comment)
    spaces(1)
    print(data)


def publish_on_profile():
    linkedin = PyLinkedinAPI(access_token)
    comment, title, description, site, image = get_content()
    data = linkedin.publish_profile(comment,
                                    title=title,
                                    description=description,
                                    submitted_url=site,
                                    submitted_image_url=image)

    spaces(1)
    print(data)


def publish_on_company():
    linkedin = PyLinkedinAPI(access_token)

    id = int(input('Enter id(integer) company: '))
    comment, title, description, site, image = get_content()

    data = linkedin.publish_company(id,
                                    comment,
                                    title=title,
                                    description=description,
                                    submitted_url=site,
                                    submitted_image_url=image)

    spaces(1)
    print(data)

while True:

    print(
        '''
        >>> 0 - Exit
        >>> 1 - Get Basic Profile
        >>> 2 - Get Companies
        >>> 3 - Get Profile with fields
        >>> 4 - Publish only text on Profile
        >>> 5 - Publish only text on Company
        >>> 6 - Publish content on Profile
        >>> 7 - Publish content on Company
        '''
    )

    op = input('Enter option: ')

    func = {
        '1': get_basic_profile,
        '2': get_companies,
        '3': get_profile,
        '4': publish_text_on_profile,
        '5': publish_text_on_company,
        '6': publish_on_profile,
        '7': publish_on_company,
    }

    if op not in func.keys():
        exit()

    try:
        func[op]()
    except Exception as ex:
        spaces(2)
        print('Error: {}'.format(ex))

