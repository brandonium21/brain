import datetime
import threading
import json
import random
import pprint
import pickle

# THE BRAIN PROJECT


## MEMORY STRUCTURE memory_bank = [ [0]{index : [ { neron_id, id, data, time }, { neron_id, id, data, time } ... ] },

time_lapse = 60
memory_counter = 0
sensory_atlas = [vision_neron, audio_neron, smell_neron, touch_neron, taste_neron]
memory_bank = []
memories_processed = 0
########################### brain process (creates memories)
def brain_function():
    mem_group = []
    memory_counter += 1
    for nerons in sensory_atlas:
        memory_frag = nerons(memory_counter)
        mem_group.append(memory_frag)
    # give memory a common iterable index
    memory = {memory_counter : mem_group}
    # put them in a memory bank
    memory_bank.append(memory)
    memories_processed += 1
    shortTerm_memory()
    return memories_processed

# call brain every x seconds
threading.Timer(time_lapse, brain_function).start()

########################### sensory system
def vision_neron(id):
    id = 0
    neron_id = v
    data = random.randint(1, 10)
    time = datetime.datetime.now()
    vdata = {'neron_id' : neron_id, 'id' : id, 'data' : data, 'time' : time}
    print data
    return json.dumps(vdata)

def audio_neron(id):
    id = 0
    neron_id = a
    data = random.randint(1, 10)
    time = datetime.datetime.now()
    adata = {'neron_id' : neron_id, 'id' : id, 'data' : data, 'time' : time}
    print data
    return json.dumps(adata)

def smell_neron(id):
    id = 0
    neron_id = s
    data = random.randint(1, 10)
    time = datetime.datetime.now()
    sdata = {'neron_id' : neron_id, 'id' : id, 'data' : data, 'time' : time}
    print data
    return json.dumps(sdata)

def touch_neron(id):
    id = 0
    neron_id = th
    data = random.randint(1, 10)
    time = datetime.datetime.now()
    thdata = {'neron_id' : neron_id, 'id' : id, 'data' : data, 'time' : time}
    print data
    return json.dumps(thdata)

def taste_neron(id):
    id = 0
    neron_id = t
    data = random.randint(1, 10)
    time = datetime.datetime.now()
    tdata = {'neron_id' : neron_id, 'id' : id, 'data' : data, 'time' : time}
    print data
    return json.dumps(tdata)


############################ memory hippocampus
def shortTerm_memory():
    ## compares past memories present memories and decides to keep or destroy.
    ### if the memory data is the same throw it out if it is different keep it  but if it is different and
    ### close to the future memory destroy it.

    present_memory = memory_bank

    ## get past memories
    pkl_file = open('memory.pkl', 'rb')
    past_memories = pickle.load(pkl_file)
    pkl_file.close()

    ## filter memories
    for mem in past_memories:
        i = 0
        i += 1
        for past_neuron in mem[i]:
            past_sensory = past_neuron['neron_id'], past_neuron['data'] 

        for curr_mem in present_memory:    
            for current_neuron in present_memory:
                current_sensory = current_neuron['neron_id'], current_neuron['data'] 
                
    ## put memory data in a pickle file
    outputmemory = open('memory.pkl', 'wb')
    pickle.dump(memory_bank, outputmemory)
    outputmemory.close()

    pass

def memory():
    ## If short term aproves after 20 to 30 sec store that list of memories in memory.
    pass

########################### preception (always search memory for familiar things then drum them up if they are familiar(3 or more nerons match))




