from parser.models.base_log import BaseLogModel

def normalize_log(source : str, raw_log : dict) -> dict:
    # for now working with a global schema, based on the source we will change it later
    try:
        parsed = BaseLogModel(**raw_log)
        return parsed.model_dump()
    except Exception as e:
        raise ValueError(f"Normalization Failed: {e}")
        
    