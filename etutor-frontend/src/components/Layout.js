import React from 'react'
import { Layout, Menu, Breadcrumb, Icon, Row } from 'antd';
import Tutor from './Tutor'
import WrappedNormalLoginForm from './LoginForm'

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;
const CustomLayout = (props) => {
    return(
        <Layout>
        <Header className="header">
          <div className="logo" />
          <Menu
            theme="light"
            mode="horizontal"
            defaultSelectedKeys={['2']}
            style={{ lineHeight: '64px' }}
          >
            <Menu.Item key="1"><span><Icon type='home'/></span>Home</Menu.Item>
            <Menu.Item key="2"><span><Icon type='book'/></span>Courses</Menu.Item>
            <Menu.Item key="3"><span><Icon type='info-circle'/></span>About Us</Menu.Item>

          </Menu>
        </Header>
        <Content style={{ padding: '0 50px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
           
          </Breadcrumb>
          <Layout style={{ padding: '24px 0', background: '#008B8B' }}>
            <Sider width={200} style={{ background: '#008B8B' }}>
              <Menu
                mode="inline"
                defaultSelectedKeys={['1']}
                defaultOpenKeys={['sub1']}
                style={{ height: '100%' }}
              >
                <SubMenu
                  key="sub1"
                  title={
                    <span>
                      <Icon type="user" />
                      Profile
                    </span>
                  }
                >
                  <Menu.Item key="1">Quizzes</Menu.Item>
                  <Menu.Item key="2">Projects</Menu.Item>
                  <Menu.Item key="3">Misc. Content</Menu.Item>
                  <Menu.Item key="4">Account Settings</Menu.Item>
                </SubMenu>
               
                <SubMenu
                  key="sub3"
                  title={
                    <span>
                      <Icon type="link" />
                      External Resources
                    </span>
                  }
                >
                  <Menu.Item key="9">option9</Menu.Item>
                  <Menu.Item key="10">option10</Menu.Item>
                  <Menu.Item key="11">option11</Menu.Item>
                  <Menu.Item key="12">option12</Menu.Item>
                </SubMenu>
              </Menu>
            </Sider>
            <Content style={{ padding: '0 24px', minHeight: 480 }}>
            <Row type="flex" justify="space-around" align="middle">
            <h1>Welcome to eTutor</h1>

            </Row>
            <WrappedNormalLoginForm/>
            </Content>
          </Layout>
        </Content>
      </Layout>
    )
}

export default CustomLayout
     

