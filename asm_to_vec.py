import numpy as np
import sys
import asm2vec.asm
import asm2vec.parse
import asm2vec.model


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def model_deserialization(s):

    tmp  = eval(s)
    model = asm2vec.model.Asm2Vec(d=200)
    tmp3 =asm2vec.internal.training.Asm2VecParams()
    tmp3.populate(tmp['params'])
    
    tmp4 = []
    for k,v in tmp['vocab'].items():
        tmpv = dict([(k.encode(),v2.encode()) if type(v2)==str else (k.encode(),v2) for k,v2 in v.items()])
        tmp5 = asm2vec.repo._deserialize_token(tmpv)
        tmp4.append((k,tmp5))
    tmp2 = asm2vec.model.Asm2VecMemento()
    tmp2.params = tmp3
    tmp2.vocab = dict(tmp4)
    model.set_memento(tmp2)

    return model

def training():
    training_funcs = asm2vec.parse.parse('out_onlockdown_5.s',func_names=['main'])
    estimating_funcs = asm2vec.parse.parse('a.s',func_names=['main'])

    
    print('# of training functions:', len(training_funcs))
    print('# of estimating functions:', len(estimating_funcs))

    model = asm2vec.model.Asm2Vec(d=200)
    training_repo = model.make_function_repo(training_funcs)
    model.train(training_repo)
    print('Training complete.')

    for tf in training_repo.funcs():
        print('Norm of trained function "{}" = {}'.format(tf.sequential().name(), np.linalg.norm(tf.v)))

    s = asm2vec.repo.serialize_vocabulary(model.memento().vocab)
    
    with open('asm2vec.model','w') as f:f.write(repr(model.memento().serialize()))

def vectorizer(fname,oname):
    estimating_funcs = asm2vec.parse.parse(fname,func_names=['main'])

    model = model_deserialization(open('asm2vec.model','r').read()) 

    #print(list(model.to_vec(estimating_funcs[0])))
    estimating_funcs_vec = list(map(lambda f: model.to_vec(f), estimating_funcs))

#    for (ef, efv) in zip(estimating_funcs, estimating_funcs_vec):
#        print(ef.name()+','+str(list(efv)))            
    with open(oname,'w') as f:
        #f.write('function_name,vector\n')
        for (ef, efv) in zip(estimating_funcs, estimating_funcs_vec):
            f.write(ef.name()+', '+str(list(efv))[1:-1]+'\n')          

def main():
#    training()
    vectorizer(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()
