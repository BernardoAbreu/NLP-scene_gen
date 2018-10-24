#!/usr/bin/env python3

import re
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


def count_indent_spaces(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            if (line.rstrip()) != '':
                line = line.replace('\t', '    ')
                spaces = len(line) - len(line.lstrip(' '))
                if len(line.lstrip(' ').rstrip()) != 0:
                    if spaces not in d.keys():
                        d[spaces] = 0
                    d[spaces] += 1
    return sorted([(k, v) for k, v in d.items()])


def remove_initial_spaces(input_file, out_file, space_list):
    remove_space = 0
    for space, count in space_list:
        if count > 10:
            remove_space = space
            break

    with open(input_file, 'r') as in_f, open(out_file, 'w') as out_f:
        for line in in_f:
            line = line.replace('\t', '    ')
            spaces = len(line) - len(line.lstrip(' '))
            if spaces >= remove_space:
                line = line[remove_space:]
            out_f.write(line)


def try_to_indent(input_file, out_file, space_list):
    sorted_space_list = [e[0] for e in sorted(space_list,
                                              key=(lambda x: (x[1], x[0])),
                                              reverse=True)
                         if e[1] > 100 or e[0] > 30]

    ssl = [e for i, e in enumerate(sorted_space_list)
           if (e - 1) not in sorted_space_list[i:] and
           (e + 1) not in sorted_space_list[i:]]

    # print(space_list)
    # print(sorted_space_list)
    # print(sorted(ssl))

    d = {}

    for s, _ in space_list:
        d[s] = min(ssl, key=lambda x: abs(x - s))

    with open(input_file, 'r') as in_f, open(out_file, 'w') as out_f:
        for line in in_f:
            try:
                spaces = len(line) - len(line.lstrip(' '))
                out_f.write(' ' * d[spaces] + line.lstrip(' '))
            except Exception:
                if spaces != 0:
                    out_f.write('\n')


def print_characters(input_file):
    # patt = re.compile(r'^[ \t]+([A-Z][A-Z\(\)\'\"0-9\. ]+)$')
    patt = re.compile(r'^[ \t]+([A-Z]\.?([A-Z\'\"0-9 ]|[A-Z)\.])+)( \([a-zA-Z0-9\(\)\'\"\. ]+\))?$')
    with open(input_file, 'r') as f:
        for line in f:
            result = patt.match(line)
            if result is not None:
                print(result.group() + ' ____ (' + input_file.split('/')[-1] + ')')
                # print(result.group()[0])


def regex_pre_process(input_file):
    with open(input_file, 'r') as f:
        movie_script = f.read()

    patt = re.compile(r'(\n[\t ]{2,}[a-zA-Z0-9\,\' \.\!\?\&\-]*[a-z0-9\,\' \-])\n\n? ?([a-zA-Z0-9\,\.\-\?\!])')

    movie_script, count = patt.subn(r'\1 \2', movie_script)
    while count:
        movie_script, count = patt.subn(r'\1 \2', movie_script)
    print(movie_script)
    # m, n = prog.subn(r'\1 \2', movie_script)
    # print(n)
    # print(m)


if __name__ == '__main__':
    input_file = sys.argv[1]
    if len(sys.argv) > 2:
        out_file = sys.argv[2]
    # print_index(input_file)
    # movie_scenes = read_script(input_file)
    # for loc, count, scene in movie_scenes:
    #     print(loc + ' - ' + str(count))
    # save_scene(out_file, movie_scenes)
    # space_count = count_indent_spaces(input_file)
    # count = len([x for x in space_count if x[1] > 100])
    # count = len(space_count)
    # if len(space_count) < 5:
    # # if count < 5:
    # print(input_file)
    # print(input_file.split('/')[-1] + '(' + str(count) + '):', end='')
    # for k, v in space_count:
    #     print(str(k) + ':' + str(v) + '  ',
    #           end='')
    # print()
    # try_to_indent(input_file, out_file, space_count)
    # remove_initial_spaces(input_file, out_file, space_count)
    # regex_pre_process(input_file)
    print_characters(input_file)
