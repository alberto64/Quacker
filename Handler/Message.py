from flask import jsonify
from Handler import DictionaryBuilder as Dic
from DAO.MessagesDAO import MessagesDAO
dao = MessagesDAO()


def getAllMessages():
    rows = dao.getAllMessages()
    if not rows:
        return jsonify(Error="No Message found"), 404
    result = []
    for row in rows:
        result.append(Dic.build_message_dict(row))
    return jsonify(Messages=result)


def getAllReacts():
    rows = dao.getAllReactions()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllLikes():
    rows = dao.getAllLikeReactions()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllDislikes():
    rows = dao.getAllDislikeReactions()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllMedias():
    rows = dao.getAllMedia()
    if not rows:
        return jsonify(Error="No media"), 404
    result = []
    for row in rows:
        result.append(Dic.build_media_dict(row))
    return jsonify(Medias=result)


def getAllTopics():
    rows = dao.getAllTopics()
    if not rows:
        return jsonify(Error="No topics"), 404
    result = []
    for row in rows:
        result.append(Dic.build_topic_dict(row))
    return jsonify(Topics=result)


def getMessageByID(mID):
    # This method return the message requested by its ID
    row = dao.getMessageInfo(mID)
    if not row:
        return jsonify(Error="Message not found"), 404
    message = Dic.build_message_dict(row)
    return jsonify(Message=message)


def getMessageReactionsByID(mID):
    # This method return the reaction of a determined message
    rows = dao.getMessageReaction(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageLikesByID(mID):
    # This method return the reaction of a determined message
    rows = dao.getMessageLike(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageDislikesByID(mID):
    # This method return the reaction of a determined message
    rows = dao.getMessageDislike(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageMedia(mID):
    # This method return the reaction of a determined message
    row = dao.getMessageMedia(mID)
    if not row:
        return jsonify(Error="Message does not contain Media"), 404
    result = Dic.build_media_dict(row)
    return jsonify(Media=result)


def getMessageTopics(mID):
    # This method return the reaction of a determined message
    rows = dao.getMessageTopics(mID)
    if not rows:
        return jsonify(Error="Message does not contain Topics"), 404
    result = []
    for row in rows:
        result.append(Dic.build_topic_dict(row))
    return jsonify(Topics=result)


def getMessageByUserID(uID):
    # This method will return the messages of a determined user
    messages = dao.getUserMessages(uID)
    if not messages:
        return jsonify(Error="User does not have any messages sent."), 404
    result_list = []
    for row in messages:
        result = Dic.build_message_dict(row)
        result_list.append(result)
    return jsonify(Messages=result_list)


def getUserReactionsBetween(uID, bDate, aDate):
    result = dao.getUserReactionsBetween(uID, bDate, aDate)
    if not result:
        return jsonify(Error = "No Reactions Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_reacted_dict(r))
    return jsonify(UserReactions=mapped_result)


def getUserReactions(uID):
    result = dao.getUserReactions(uID)
    if not result:
        return jsonify(Error = "No Reactions Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_reacted_dict(r))
    return jsonify(UserReactions=mapped_result)


def getUserMessagesBetween(uID, bDate, aDate):
    result = dao.getUserMessagesBetween(uID, bDate, aDate)
    if not result:
        return jsonify(Error = "No Messages Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_message_dict(r))
    return jsonify(UserMessagesBetween=mapped_result)


def getUserMessages(uID):
    result = dao.getUserMessages(uID)
    if not result:
        return jsonify(Error = "No Messages Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_message_dict(r))
    return jsonify(UserMessages=mapped_result)

def getUserTopics(uID):
    result = dao.getUserTopics(uID)
    if not result:
        return jsonify(Error = "No Topics Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_topic_dict(r))
    return jsonify(UserTopics = mapped_result)


def getUserTopicsBetween(uID, bDate, aDate):
    result = dao.getUserTopicsBetween(uID, bDate, aDate)
    if not result:
        return jsonify(Error = "No Topics Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_topic_dict(r))
    return jsonify(UserTopics = mapped_result)


def getMessagesByChatID(cID):
    # This method will return the messages in a determined  chat
    chat_messages = dao.getChatMessages(cID)
    if not chat_messages:
        return jsonify(Error="No Messages Found")
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages=result_messages)

def getChatMediaByID(cid):
    media = dao.getChatMedia(cid)
    if not media:
        return jsonify(Error="No Media Found")
    result_list = []
    for row in media:
        result = Dic.build_media_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)

def getChatTopicByID(cid):
    media = dao.getChatTopics(cid)
    if not media:
        return jsonify(Error="No Media Found")
    result_list = []
    for row in media:
        result = Dic.build_topic_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)