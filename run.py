import pytest
from Tools import Shell

if __name__ == "__main__":
    
    # 测试集
    item = 'test_case'

    test_case_path = './TestCase/{}.py'.format(item)
    data_path = 'Report/{}/json'.format(item)
    html_path = 'Report/{}/html'.format(item)

    # 测试
    args = ['-s', '-q',test_case_path, '--alluredir', data_path]
    pytest.main(args)

    # 生成html文件
    cmd = 'allure generate %s -o %s' % (data_path, html_path)
    shell = Shell.Shell()
    shell.invoke(cmd)