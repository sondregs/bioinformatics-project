import jpredapi


def submit_jpred(sequence):
    return jpredapi.submit(mode="single", user_format="raw", seq=sequence)


def results_jpred():
    return jpredapi.get_results("jp_HTOd8x2", results_dir_path="jpred_sspred/results", extract=True)


def status_jpred(jobid):
    return jpredapi.status(jobid)
