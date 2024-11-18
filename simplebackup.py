import gitlab
import subprocess

# 配置 GitLab 实例和认证信息
gl = gitlab.Gitlab(private_token='', url='https://gitlab.com')

# 指定要克隆的组 ID
group_id = ''

# 获取指定组
group = gl.groups.get(group_id)

# 克隆组内所有项目
for project in group.projects.list(include_subgroups=True,get_all=True):
    print(f"正在克隆项目: {project.name}")
    subprocess.run(['git', 'clone', project.http_url_to_repo, project.name])

# 递归克隆子组中的所有项目
#def clone_projects_in_subgroup(subgroup):
#    for project in subgroup.projects.list(get_all=True):
#        print(f"正在克隆子组项目: {project.name}")
#        subprocess.run(['git', 'clone', project.http_url_to_repo, project.name])
#    for subgroup in subgroup.subgroups.list(get_all=True):
#        clone_projects_in_subgroup(subgroup)

# 克隆所有子组中的项目
#for subgroup in group.subgroups.list(get_all=True):
#    print(f"正在处理子组: {subgroup.name}")
#    clone_projects_in_subgroup(subgroup)
