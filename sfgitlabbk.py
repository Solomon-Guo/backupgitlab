import requests
import os

# GitLab服务器地址
GITLAB_URL = 'https://gitlab.com'
# 组的名称
GROUP_NAME = 'x'
# 访问令牌，用于身份验证
ACCESS_TOKEN = ''

# 构建API请求URL
api_url = f'{GITLAB_URL}/api/v4/groups/platform-software/{GROUP_NAME}/projects'

# 设置身份验证头
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# 发送GET请求获取组下的所有项目信息
response = requests.get(api_url, headers=headers)

# 解析响应json数据
project_infos = response.json()

# 遍历所有项目信息，并克隆项目
for project_info in project_infos:
    project_url = project_info['http_url_to_repo']
    project_name = project_info['name']
    project_dir = f'C:/{project_name}'

    # 克隆项目
    os.system(f'git clone --recursive {project_url} {project_dir}')
