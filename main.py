from flask import Flask, jsonify, request
from Handler import Chat
from Handler import Message
from Handler import User
from mainpage import mainpage
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def mainPage():
    return mainpage


# ==================== User Methods ====================== #
@app.route('/users', methods=['GET'])
#WORKS
def getAllUsers():
    if request.method == 'GET':
        result = User.getAllUsers()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/<int:uid>', methods=['GET'])
#WORKS
def getUserByID(uid):
    if request.method == 'GET':
        result = User.getUserInfo(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/active', methods=['GET'])
#WORKS
def getAllUsersByActivity():
    if request.method == 'GET':
        result = User.getActiveUsers()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/message/liked/<int:mid>', methods=['GET'])
#WORKSS
def getUsersByLikedMessage(mid):
    if request.method == 'GET':
        result = User.getUsersByLikedMessage(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/message/disliked/<int:mid>', methods=['GET'])
#WORKSSSS
def getUsersByDisLikedMessage(mid):
    if request.method == 'GET':
        result = User.getUsersByDislikedMessage(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/chat/<int:cid>', methods=['GET'])
#WORKSSS
def getMembersByChatID(cid):
    if request.method == 'GET':
        result = User.getMembersByChatID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/chat/admin/<int:cid>', methods=['GET'])
#WORKS
def getAdminByChatID(cid):
    if request.method == 'GET':
        result = User.getAdminByChatID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# =================== Credential Methods ================= #
@app.route('/credentials', methods=['GET'])
#WORKSS
def getCredentials():
    if request.method == 'GET':
        result = User.getAllCredentials()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/credentials/user/<int:uid>', methods=['GET'])
#WORKSSS
def getUserCredentialByID(uid):
    if request.method == 'GET':
        result = User.getUserCredentials(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Activity Methods ======================= #
@app.route('/activities', methods=['GET'])
#WORKSSS
def getAllActivities():
    if request.method == 'GET':
        result = User.getAllActivity()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/activities/user/<int:uid>', methods=['GET'])
#WORKSSSSSS
def getUserActivityByID(uid):
    if request.method == 'GET':
        result = User.getUserActivity(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Contact Methods ======================== #
@app.route('/contacts', methods=['GET'])
#WORKSSSS
def getAllContacts():
    if request.method == 'GET':
        result = User.getAllContacts()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/contacts/user/<int:uid>', methods=['GET'])
#WORKSS
def getUserContactsByID(uid):
    if request.method == 'GET':
        result = User.getUserContacts(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Chat Methods ===================== #
@app.route('/chats', methods=['GET'])
#WORKSSS
def getAllChats():
    if request.method == 'GET':

        result = Chat.getAllChats()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/<int:cid>', methods=['GET'])
#WORKSSSS
def getChatByID(cid):
    if request.method == 'GET':
        result = Chat.getChatByID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/user/<int:uid>', methods=['GET'])
#WORKSSSS
def getUserChatsByID(uid):
    if request.method == 'GET':

        result = Chat.getChatByUserID(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/admin/<int:uid>', methods=['GET'])
#WORKSSS
def getChatsAsAdminByID(uid):
    if request.method == 'GET':

        result = Chat.getChatAsAdmin(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/active', methods=['GET'])
#WORKSSS
def getActiveChats():
    if request.method == 'GET':
        result = Chat.getAllActiveChats()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/chats/groupchats', methods = ['GET'])
#workd
def getGroupChats():
    if request.method == 'GET':
        result = Chat.getGroupChats()
        return result
    else:
        return jsonify(Error = "Method not allowed"), 404

# ============== Participant Methods ================== #
@app.route('/participants', methods=['GET'])
#WORKSSSS
def getAllParticipants():
    if request.method == 'GET':
        result = Chat.getALlParticipants()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/participants/chat/<int:cid>', methods=['GET'])
#WORKSSS
def getChatParticipantsByID(cid):
    if request.method == 'GET':
        result = Chat.getParticipantsByChatID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Message Methods ====================== #
@app.route('/messages', methods=['GET'])
#WORKS
def getAllMessages():
    if request.method == 'GET':
        result = Message.getAllMessages()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/<int:mid>', methods=['GET'])
def getMessageByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/chat/<int:cid>', methods=['GET'])
def getMessageByChatID(cid):
    #WORKSSS
    if request.method == 'GET':
        result = Message.getAllChatMessages(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/active/chat/<int:cid>', methods=['GET'])
def getActiveMessageByChatID(cid):
    #WORKS
    if request.method == 'GET':
        result = Message.getAllChatactiveMessages(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/user/<int:uid>', methods=['GET'])
def getMessageByUserID(uid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageByUserID(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/chat/<int:cid>/user/<int:uid>', methods=['GET'])
def getMessageInChatByUser(cid, uid):
    #WORKSSS
    if request.method == 'GET':
        result = Message.getAllUserMessagesInChat(uid, cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# =============== Topic Methods ======================== #
@app.route('/topics', methods=['GET'])
#WORKS
def getAllTopics():
    if request.method == 'GET':
        result = Message.getAllTopics()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/message/<int:mid>', methods=['GET'])
def getMessageTopicsByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageTopics(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/user/<int:uid>', methods=['GET'])
def getAllTopicsByUser(uid):
    #WORKS
    if request.method == 'GET':
        result = Message.getAllTopicsByUser(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/chat/<int:cid>', methods=['GET'])
def getChatTopicsByID(cid):
    #WORKS
    if request.method == 'GET':
        result = Message.getChatTopicByID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ==================== Media Methods ========================= #
@app.route('/medias', methods=['GET'])
def getAllMedia():
    #WORKS
    if request.method == 'GET':
        result = Message.getAllMedias()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/message/<int:mid>', methods=['GET'])
def getMessageMediaByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageMedia(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/chat/<int:cid>', methods=['GET'])
def getChatMediaByID(cid):
    #WORKS
    if request.method == 'GET':
        result = Message.getAllMediaInChat(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/user/<int:uid>', methods=['GET'])
def getUserMediaByID(uid):
    #WORKS
    if request.method == 'GET':
        result = Message.getAllMediaByUser(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================ Reaction Methods ===================== #
@app.route('/reactions', methods=['GET'])
def getAllReactions():
    #WORKS
    if request.method == 'GET':
        result = Message.getAllReacts()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like', methods=['GET'])
def getAllLikes():
    #WORKS
    if request.method == 'GET':
        result = Message.getAllLikes()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike', methods=['GET'])
#WORKS
def getAllDislikes():
    if request.method == 'GET':
        result = Message.getAllDislikes()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/message/<int:mid>', methods=['GET'])
def getAllReactionsInMessage(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getAllReactionsInMessage(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/user/<int:uid>', methods=['GET'])
def getUserReactions(uid):
    #WORKS
    if request.method == 'GET':
        result = Message.getUserReactions(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like/message/<int:mid>', methods=['GET'])
def getMessageLikeByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageLikesByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike/message/<int:mid>', methods=['GET'])
def getMessageDisLikeReactionsByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageDislikesByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/count/message/<int:mid>', methods=['GET'])
def getMessageReactionsCountByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageReactionsCountByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like/count/message/<int:mid>', methods=['GET'])
def getMessageLikeReactionsCountByID(mid):
    #WORKS
    if request.method == 'GET':
        result = Message.getMessageLikesCountByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike/count/message/<int:mid>', methods=['GET'])
def getMessageDisLikeReactionsCountByID(mid):
    #WORKS
    #displays a positive number
    if request.method == 'GET':
        result = Message.getMessageDislikesCountByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


if __name__ == '__main__':
    app.run()
