#!/usr/bin/env python

import sys

TRANSITIONS = ('CUT TO', 'FADE IN', 'FADE OUT')


def read_script(filename):
    movie = []
    scene = ''
    last_location = ''
    count = 0
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            is_location = False
            line = line.rstrip()
            lstrip_line = line.lstrip()
            lstrip_line_up = lstrip_line.upper()
            if any(loc in lstrip_line for loc in ('INT.', 'EXT.')):
                is_location = True

            if any(t in lstrip_line_up for t in TRANSITIONS) or is_location:
                movie.append((last_location, count, scene))
                scene = ''
                i += 1
                count = 0
                if is_location:
                    scene += line
                    last_location = lstrip_line
                else:
                    movie.append(('TRANSITION', 0, ''))

            count += len(lstrip_line_up.rstrip().replace(' ', ''))
        movie.append((last_location, count, scene))
    return movie


def print_index(filename):
    location = ''
    last_location = ''
    count = 0
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            is_new_location = False
            strip_line = line.lstrip().rstrip()
            cur_count = len(strip_line.replace(' ', ''))
            strip_line_up = strip_line.upper()

            if strip_line[:4] in ('INT.', 'EXT.'):
                has_flashback = 'FLASHBACK' in strip_line_up
                is_continuous = 'CONTINUOUS' in strip_line_up
                location = strip_line.split()
                # print('last_location: ' + last_location)
                is_new_location = not (has_flashback or is_continuous or
                                       location[1] in last_location)
                if not has_flashback:
                    last_location = strip_line

            if 'CUT TO' in strip_line_up or 'FADE IN' in strip_line_up or \
                    'FADE OUT' in strip_line_up or is_new_location:

                print('last_count: ' + str(count) + '\n')
                count = 0
                print(str(i) + ': ' + strip_line)
                i += 1
            else:
                if strip_line[:4] in ('INT.', 'EXT.'):
                    print('\t' + strip_line)
            count += cur_count


def print_index2(filename):
    last_location = ''
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line = line.lstrip()
            if line[:4] in ('INT.', 'EXT.'):
                location = line.lstrip().split()
                if 'CONTINUOUS' in line.upper() or \
                    'FLASHBACK' in line.upper() or \
                        location[1] in last_location:
                    print('\t' + line)
                else:
                    print(line)
                    last_location = line


def save_scene(out_file, scenes):
    for scene_name, scene in enumerate(scenes):
        with open(out_file + 'scene_' + str(scene_name), 'w') as f:
            f.write(scene)


if __name__ == '__main__':
    input_file = sys.argv[1]
    # out_file = sys.argv[2]
    # print_index(input_file)
    movie_scenes = read_script(input_file)
    for loc, count, scene in movie_scenes:
        print(loc + ' - ' + str(count))
    # save_scene(out_file, movie_scenes)
