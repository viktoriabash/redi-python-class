import requests.exceptions
from pydog_exercise import get_all_breeds, get_random_image, get_images_by_breed

errors = 0

try:
    assert get_all_breeds()['australian'] == ['kelpie', 'shepherd']
except:
    errors += 1
    print('Error in get_all_breeds()')

try:
    assert get_all_breeds()['non-existing-dog'] == ['kelpie', 'shepherd']
except:
    errors += 1
    print('Error in get_all_breeds(), function should throw an exception!')

try:
    assert get_random_image().endswith('.jpg')
except:
    errors += 1
    print('Error in get_random_image()')

try:
    assert get_images_by_breed('beagle')[2].split('/')[-2] == 'beagle'
except:
    errors += 1
    print('Error in get_image_by_breed()')

try:
    get_images_by_breed('atika')
    raise NotImplementedError('Error in get_images_by_breed(), function should throw an exception!')
except requests.exceptions.RequestException as e:
    pass
except NotImplementedError as e:
    errors += 1
    print(e)


if errors == 0:
    print('\nYou implemented all functions correctly!')
else:
    print(f'There are still {errors} errors.')
