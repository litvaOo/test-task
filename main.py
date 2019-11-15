import sys, os, re
import lxml
import lxml.html as html

if __name__ == "__main__":
    origin_file_path = sys.argv[1]
    diff_file_path = sys.argv[2]
    page = html.parse(origin_file_path)
    home = page.getroot()
    button = home.get_element_by_id("make-everything-ok-button")
    button_xpath = page.getpath(button)
    button_xpath =  re.sub(r'.\d.', '', button_xpath, 0)
    diff_element = None
    diff_page = html.parse(diff_file_path)
    parent_tree_depth = -1
    xpath_splitted = button_xpath.split("/")
    while not diff_element:
        current_parent = diff_page.xpath('/'.join(xpath_splitted[:parent_tree_depth]))
        if len(current_parent) > 1:
            for parent in current_parent:
                try:
                    diff_element = parent.xpath(f"//a[@id='{button.items()[0][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
                try:
                    diff_element = parent.xpath(f"//a[@class='{button.items()[1][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
                try:
                    diff_element = parent.xpath(f"//a[@href='{button.items()[2][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
                try:
                    diff_element = parent.xpath(f"//a[@title='{button.items()[3][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
                try:
                    diff_element = parent.xpath(f"//a[@rel='{button.items()[4][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
                try:
                    diff_element = parent.xpath(f"//a[@onclick='{button.items()[5][1]}']")
                    print(diff_page.getpath(diff_element[0]))
                    sys.exit(0)
                except Exception as e:
                    pass
        else:
            try:
                diff_element = current_parent[0].xpath(f"//a[@id='{button.items()[0][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
            try:
                diff_element = current_parent[0].xpath(f"//a[@class='{button.items()[1][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
            try:
                diff_element = current_parent[0].xpath(f"//a[@href='{button.items()[2][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
            try:
                diff_element = current_parent[0].xpath(f"//a[@title='{button.items()[3][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
            try:
                diff_element = current_parent[0].xpath(f"//a[@rel='{button.items()[4][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
            try:
                diff_element = current_parent[0].xpath(f"//a[@onclick='{button.items()[5][1]}']")
                print(diff_page.getpath(diff_element[0]))
                sys.exit(0)
            except Exception as e:
                pass
        parent_tree_depth -= 1