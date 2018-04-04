from flask import jsonify

from Handler import DictionaryBuilder as Dic
from DAO.ChatDAO import ChatDAO

dao = ChatDAO()


def getAllChats():
    # This method will return all the chats

    chat_lists = dao.getAllChats()
    if not chat_lists:
        return jsonify(Error="No Records Found")
    result_list = []
    for row in chat_lists:
        result = Dic.build_chat_dict(row)
        result_list.append(result)
    return jsonify(Chat=result_list)


def getChatByID(cID):
    # This method will return the determined chat by its ID
    row = dao.getChatByID(cID)
    if not row:
        return jsonify(Error=" Chat not found"), 404
    chat = Dic.build_chat_dict(row)
    return jsonify(Chat=chat)


def getParticipantsByChatID(cID):
    # This method returns the list of participants in a determined chat
    chat_participants = dao.getChatParticipants(cID)
    if not chat_participants:
        return jsonify(Error="No Participants Found")
    result_list = []
    for row in chat_participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants=result_list)


def getChatByUserID(uID):
    # This method will return the chats on which the user are part of
    chats = dao.getChatByUserID(uID)
    if not chats:
        return jsonify(Error="No Chats Found")
    result_list = []
    for row in chats:
        result = Dic.build_chat_dict(row)
        result_list.append(result)
    return jsonify(Chats=result_list)


def getALlParticipants():
    # This method will return all the participants on the application
    participants = dao.getAllParticipants()
    if not participants:
        return jsonify(Error="No Participants Found")
    result_list = []
    for row in participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants=result_list)

def getChatAsAdmin(uID):
    result = dao.getChatsAsAdmin(uID)
    if not result:
        return jsonify(Error="No Chats Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_chat_dict(r))
    return jsonify(AdminChats=mapped_result)

def getChatAsMember(uID):
    result = dao.getChatAsMember(uID)
    if not result:
        return jsonify(Error="No Chats Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_participants_dict(r))
    return jsonify(MemberChats=mapped_result)

#   def removeChatGroup(self,cID):
#      #THis method will remove a chat
#        dao = ReadChatDAO()
#       if not dao.getChatInfo(cID):
#            return jsonify(Error = "Chat not found"), 404
#       else:
#            #CHECKKKKKKKKKKKK!!-!-!_!_!_!_1!_!!-!:D
#            dao.getAllChats().__getitem__(cID).insert(5, False)
