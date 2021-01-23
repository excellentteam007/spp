import os

class Start:

    def load(self):
        module_names = os.listdir('..\\kwdriver')
        test_module_names = []
        for module in module_names:
            if module.endswith('_test.py'):
                test_module_names.append(module)

        return test_module_names

    def load1(self):
        test_module_names = self.load()
        for module_name in test_module_names:
            module_name = module_name.split('.')[0]
            module = __import__('WTFV1.kwdriver.'+module_name, fromlist=module_name)
            contents = dir(module)
            class_names = []
            for content in contents:
                if content.endswith('Test'):
                    class_names.append(content)
            class_objs = []
            for class_name in class_names:
                if hasattr(module, class_name):
                    class_obj = getattr(module, class_name)
                    # print(class_obj)
                    class_objs.append(class_obj)
            # print(class_objs)
            contents = []
            for obj in class_objs:
                contents = dir(obj)
                # contents.append(contents1)
            test_module_names = []
            for content in contents:
                if content.startswith('test_'):
                    test_module_names.append(content)

            for obj in class_objs:
                o = obj()
                for method_name in test_module_names:
                    if hasattr(obj, method_name):

                        getattr(o, method_name)()

                # print(obj)









if __name__ == '__main__':
    Start().load1()
