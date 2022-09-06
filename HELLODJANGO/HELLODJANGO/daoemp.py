import pymysql

class DaoEmp :
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', port=3305
                                    ,password='python', db='python',charset='utf8')

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def mylist(self):
        sql = "select * from emp"

        self.cur.execute(sql)

        mylist = self.cur.fetchall()
        return mylist
    
    def myone(self,e_id):
        sql = f"""
        SELECT e_id, e_name,sex,addr
        FROM emp
        where
        e_id='{e_id}'"""
        self.cur.execute(sql)
        
        mylist = self.cur.fetchall()
        return mylist[0]
    
    def myinsert(self,e_id,e_name,sex,addr):
        sql = f"""insert into emp(e_id, e_name,sex,addr)
        values('{e_id}','{e_name}','{sex}','{addr}') """
        
        cnt=self.cur.execute(sql)
        
        self.conn.commit()
        return cnt
    
    def myupdate(self,e_id,e_name,sex,addr):
        sql = f"""update emp set e_name ={e_name},sex = {sex}, addr={addr}
        where e_id ={e_id}"""
        cnt = self.cur.execute(sql)
        
        self.conn.commit()
        
        return cnt
    
    def mydelete(self,e_id):
        sql = f"""delete from emp where e_id={e_id}"""
        
        cnt = self.cur.execute(sql)
        
        self.conn.commit()
        
        return cnt 
        
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ =='__main__':
    de = DaoEmp()
    cnt = de.mydelete('4')
    print('cnt',cnt)
        