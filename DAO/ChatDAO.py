"""
This Class contain DAO methods for the entities of Chats and Participants
"""
import psycopg2
from pg_config import pg_config


class ChatDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'],
                          pg_config['port'], pg_config['host'])
        self.conn = psycopg2._connect(connection_url)


    # ============================== Create Methods ============================= #
    def insertChat(self, cName, isGroupChat, adminID):
        #THis method creates a new chat on the database

        cursor = self.conn.cursor()
        query = " insert into chats(cname,ctime,isGroupChat,isActive,uid)"\
                "values(%s,'now',%s,'t',%s) returning cid"
        cursor.execute(query,(str(cName),str(isGroupChat),adminID))
        cid = cursor.fetchone()
        self.conn.commit()
        query2="insert into participants(cid,uid,ptime) values(%s,%s,'now');"
        cursor.execute(query2,(cid,adminID))
        self.conn.commit()
        return cid

    def insertParticipant(self, cID, uID,contact):
        #TODO make sure that this method works, it is done as in the PartApp of professor
        # Insert a participant to a chat
        cursor = self.conn.cursor()
        query = "select count(*) from contacts where uid = %s and memberid = %s"
        cursor.execute(query,(uID,contact))
        isContact = cursor.fetchone()
        self.conn.commit()
        if isContact==0:
            return None
        else:
            query2 = "select count(*) from participants where uid = %s and cid = %s"
            cursor.execute(query2,(uID,cID))
            isParticipant = cursor.fetchone()
            self.conn.commit()
            if isParticipant[0]!=1:
                return None
            else:
                query3 = "insert into participants(cid,uid,ptime) values(%s,%s,'now') returning ptime"
                cursor.execute(query3,(cID,contact))
                ptime = cursor.fetchone()
                self.conn.commit()
        return ptime

    def getTimeForParticipantInsertion(self,uid):
        #This method returns the time the user was added to the system
        cursor = self.conn.cursor()
        query2 = "select ptime from participants where uid = %s"
        cursor.execute(query2,uid)
        ptime = cursor.fetchone()
        self.conn.commit()
        return ptime

    def getChatParticipant(self,cid, uid):
        #This method returns the time the user was added to the system
        cursor = self.conn.cursor()
        query2 = "select * from participants where uid = %s and cid = %s"
        cursor.execute(query2, (uid, cid))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    # ============================= Get Methods ================================= #
    def getAllChats(self):
        # This method will return all the chats
       #WORKSSSSSSSSSSSSS
        cursor = self.conn.cursor()
        query = "select * from chats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllActiveChats(self):
        # This method will return all the chats
        #WORKSSSSSSSSSSSSS
        cursor = self.conn.cursor()
        query = "select * from chats where isActive=true"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatByUserID(self, uID):
    #This method will return the chats on which that user is in
    #WORKSSSSS
        cursor = self.conn.cursor()
        query = "select * from chats where cid in (select cid from participants where uid = %s);"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllParticipants(self):
        # This method will give all the participants in the application
        #WORKSSSSSSSSSSSS
        cursor = self.conn.cursor()
        query = "select * from participants;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatParticipants(self,cID):
        # THis method will return the active participants of a specified chat ( active or nonactive chat)
        #WORKSSSSSSSSS
        cursor = self.conn.cursor()
        query = " select uid, cid, ptime from participants natural inner join users where cID = %s;"
        cursor.execute(query,(cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatActivePartipants(self,cID):
        # This method will give the active participants in a desired chat
        cursor = self.conn.cursor()
        query = "select * from activities natural inner join users natural inner join messages where cID =  %s and isActive = true;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatNonActiveParticipants(self,cID):
        # This method will return the non active users in a certain chat
        cursor = self.conn.cursor()
        query = "select * from activities natural inner join users natural inner join messages where cID =  %s and isActive = false;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatInfo(self,cID):
        # This method will return the information of a desired chat
        cursor = self.conn.cursor()
        query = " select * from chats where cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatWithMedia(self,mID):
        # This method will return the chat on which determined media is located in
        cursor = self.conn.cursor()
        query = " select *  from messages natural inner join medias where mid = %s;"
        cursor.execute(query,(mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatsByTopic(self,hashtag):
        # This method will return the chats on which the hashtag was sent
        cursor = self.conn.cursor()
        query = "select *  from messages natural inner join topics where hashtag =%s;"
        cursor.execute(query,(hashtag,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatByID(self,cID):
        # This method will return the chat given its ID
        cursor = self.conn.cursor()
        query = "select * from chats where cid=%s;"
        cursor.execute(query,(cID,))
        result = []
        result = cursor.fetchone()
        return result


    def getChatsAsAdmin(self, uID):
    #Returns a list with the chats of the admin user with ID uID
    #WORKSSSS
       cursor = self.conn.cursor()
       query = "select * from chats where uid=%s;"
       cursor.execute(query,(uID,))
       result = []
       for row in cursor:
        result.append(row)
        return result

    def getGroupChats(self):
        #THis method returns all the group chats in the database
        cursor = self.conn.cursor()
        query = " select * from chats where isGroupchat = true;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getChatsDeleted(self):
        # This method will return the deleted chats
        return []

    # Returns the list of all chats which the user with ID uID is member of.
    def getChatAsMember(self, uID):
        return []

    # ======================= Update Methods ========================== #
    def updateChat(self, cID, cName, cDate, cTime, isGroupChat, adminID):
        # This method is supposed to be used to change the chat name
        # Also to that its admin 'deletes' chats by changing it to false
        return cID

    # ======================= Delete Methods ========================= #
    def deleteChat(self, cID):
        # Remove a chat
        return cID

    def deleteParticipant(self, cID, uID,admin):
        # Remove an user from a chat,only by the admin of the chat
        cursor = self.conn.cursor()
        query = "select count(*) from chats where cid = %s and uid = %s;"
        print("query1")
        cursor.execute(query,(cID,admin))
        isAdmin = cursor.fetchone()
        self.conn.commit()
        print(isAdmin)
        if isAdmin[0]==1:
            query2 = "DELETE from participants where cid = %s and uid = %s returning uid;"
            print("query2")
            cursor.execute(query2,(cID,uID))
            userDeleted = cursor.fetchone()
            self.conn.commit()
            return userDeleted
        else:
         return None

