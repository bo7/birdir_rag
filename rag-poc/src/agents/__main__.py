\"\"\"CLI entrypoint for orchestrating our Google ADK agents\"\"\"
import agents

def run_query_flow(nl_query):
    # TODO: instantiate SequentialAgent → ParallelAgent per our design
    pass

if __name__ == '__main__':
    import fire
    fire.Fire(run_query_flow)
