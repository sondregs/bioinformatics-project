import jpredapi


def submit_jpred():
    return jpredapi.submit(mode="single", user_format="raw", seq="MQVWPIEGIKKFETLSYLPPLTVEDLLKQIEYLLRSKWVPCLEFSKVGFVYRENHRSPGYYDGRYWTMWKLPMFGCTDATQVLKELEEAKKAYPDAFVRIIGFDNVRQVQLISFIAYKPPGC")# , seq="MQVWPIEGIKKFETLSYLPP")


def results_jpred():
    return jpredapi.get_results("jp_HTOd8x2", results_dir_path="jpred_sspred/results", extract=True)


def status_jpred(jobid):
    return jpredapi.status(jobid)
