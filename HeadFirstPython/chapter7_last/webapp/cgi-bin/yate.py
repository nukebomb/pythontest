from string import Template
# 从标准库的'string'模块导入'Template'类。它支持简单的字符串替换模板


def start_response(resp='text/html'):
    return('Countent-type: ' + resp + '\n\n')
# 这个函数需要一个字符串作为参数，用它来创建一个CGI


def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
    # 这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中
    # 页面本身存储在一个单独的文件'templa/header.html'


def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + \
            the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
    # 与'include_header' 函数类似，这个函数使用一个字符串最为参数，
    # 创建HTML页面的尾部。页面本身存储在一个单独文件中


def start_form(the_url, form_type='POST'):
    return ('<form action="' + the_url + '"method="' + form_type + '">')
    # 返回部分表单


def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
    # 返回表单的后半部分


def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name + '" value="' + rb_value + '"> ' + rb_value + '<br />')
    # 返回单选按钮


def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
    # 返回一个无序列表


def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>')

def para(para_text):
  return('<p>' + para_text + '</p>')
