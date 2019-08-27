picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# 'I am bringing 2 cups.'
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# 'I am bringing 0 eggs.'