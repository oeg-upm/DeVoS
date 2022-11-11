import argparse
import traceback

from ogister.gister import workflow, draw_diagrams, freq_workflow, leng_workflow
import os
import json
from datetime import datetime
import rdflib

# meta_srcs = ["title", "description", "abstract"]
meta_srcs = ["abstract"]


def save_json(json_path, classes, relations, meta):
    """
        Generate a json file of the gist. This is mainly used for evaluation purposes
    """
    j = {
        "classes": classes,
        "relations": relations,
        "meta": meta,
    }

    # json_string = json.dumps(j)
    with open(json_path, 'w') as outfile:
        json.dump(j, outfile)
        # json.dump(json_string, outfile)


def save_label_len(d, out_path):
    with open(out_path, 'w') as f:
        for k in d:
            f.write("%s,%d\n" % (k, d[k]))


def experiment(input_files, output_path, only_object_property, freq, topn, leng, lang=None, max_options=0):
    """
    Experiment
    """
    global meta_srcs

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if freq:
        meta_srcs = ["freq-%d" % topn]
    elif leng:
        meta_srcs = ["leng-%d" % topn]

    for inp in input_files:
        if os.path.isdir(inp):
            print("skip: %s" % inp)
            continue
        for m in meta_srcs:
            titl = desc = abst = False
            if m == "title":
                titl = True
            elif m == "description":
                titl = desc = True
            elif m == "abstract":
                titl = desc = abst = True
            elif m.startswith("freq"):
                pass
            elif m.startswith("leng"):
                pass
            else:
                raise Exception("invalid meta src")

            graph_fname_base = inp.split(os.sep)[-1]+"-"+m
            check_diagram_fpath = os.path.join(output_path, graph_fname_base + ".md")
            if os.path.exists(check_diagram_fpath):
                print("\n%s already exists" % check_diagram_fpath)
                continue
            try:
                if freq:
                    classes, relations = freq_workflow(input_path=inp, out_path=None,
                                                       only_object_property=only_object_property, topn=topn)
                elif leng:
                    classes, relations, class_leng_dict = leng_workflow(input_path=inp, out_path=None, topn=topn)
                    label_len_path = os.path.join(output_path, graph_fname_base + ".csv")
                    save_label_len(class_leng_dict, label_len_path)
                else:
                    classes, relations = workflow(input_path=inp, out_path=None, lang=lang, max_options=max_options,
                                                  title=titl, desc=desc, abstract=abst,
                                                  only_object_property=only_object_property)
            except Exception as e:
                print("Error processing: %s" % inp)
                print("Exception: %s" % str(e))
                traceback.print_exc()
                continue
            graph_fname = graph_fname_base
            opath = os.path.join(output_path, graph_fname + ".md")
            json_path = os.path.join(output_path, graph_fname + ".json")
            # label_path = os.path.join(output_path, graph_fname + ".csv")
            draw_diagrams(classes=classes, relations=relations, out_path=opath)
            save_json(json_path, classes=classes, relations=relations, meta=m)
            # save_label_len(label_path, classes=classes)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('-m', '--maxoptions', default=0, help="Maximum number of meta literal for each meta type (e.g., title)")
    parser.add_argument('--object-property', action="store_true", help="Whether to only use object property for getting the relevant properties relenvant to the given meta")
    parser.add_argument('-f', '--freq', action="store_true", help="Use frequency to fetch the most relative classes and properties")
    parser.add_argument('-g', '--leng', action="store_true", help="Use the length to fetch the most relevant classes and properties")
    parser.add_argument('-n', '--topn', default=0, type=int, help="The maximum number of relevant classes.")

    args = parser.parse_args()
    return args.output, args.input, args.lang, int(args.maxoptions), args.object_property, args.freq, args.topn, args.leng


def main():
    """
    Parse Arguments
    """
    a = datetime.now()
    output_path, input_files, lang, max_options, only_object_property, freq, topn, leng = parse_arguments()
    experiment(input_files, output_path, lang=lang, max_options=max_options, only_object_property=only_object_property,
               freq=freq, topn=topn, leng=leng)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()

