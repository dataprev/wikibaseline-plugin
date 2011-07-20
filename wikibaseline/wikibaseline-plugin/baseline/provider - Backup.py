if model.inserirBaseline():
            data["info"] = "Cadastro efetuado com sucesso!"
            id = model.getBaselineByName(nome)
    
            for x in check:
                dados = x.split("+")
                itemBase = itemBaseline(self.env,id[0][0],dados[0],dados[1])
                itemBase.inserirItemBaseline()           
        else:
            data["info"] = "Nao foi possivel efetuar cadastro!"          
            return 'teste.html', data, None
    
    
        # This tuple is for Genshi (template_name, data, content_type)
        # Without data the trac layout will not appear.                
        add_stylesheet(req, 'hw/css/baseline.css')
        return 'baseline.html', data, None        
    
        