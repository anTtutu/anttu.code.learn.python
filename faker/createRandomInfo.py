# -*- coding:utf-8 -*-

from faker import Faker

# faker是个很好的测试工具，随机生成很多看着很真实的信息，比如姓名 地址 公司名 邮箱 手机号 身份证号等

faker = Faker('zh_cn')

for i in range(100):
    print(faker.name())
    # print(faker.sex())
    print(faker.phone_number())
    print(faker.text())
    print(faker.profile())
    print(faker.uuid4())