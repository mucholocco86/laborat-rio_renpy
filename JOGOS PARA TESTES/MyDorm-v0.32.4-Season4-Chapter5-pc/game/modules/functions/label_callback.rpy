init +100 python:
    if not "labels_seen" in globals ():
        labels_seen = []
    oldLabelCallback = config.label_callback                        # we store the old label_callback (if it exists) to be able to call it in our new callback
    def newLabelCallback (labelName, isJumpOrCall):
        if oldLabelCallback:                                        # execute old label callback
            oldLabelCallback (labelName, isJumpOrCall)
        global currentLabel, labelsSeen, labels_seen, excludedLabels
        currentLabel = labelName                                    # just so we can access the current labels name
###
# compatibility of old labels_seen
        if isinstance (labels_seen, list) and len (labels_seen) > 0:
            labelsSeen += labels_seen
            labels_seen = []
###
        if not isJumpOrCall or labelName.startswith ("_") or labelName.startswith ("c_") or labelName in excludedLabels:         # we only do stuff if we jumped to or called the labels
            return
        labelsSeen.extend ([ labelName ])
        labelsSeen = list (dict.fromkeys (labelsSeen))          # remove duplicates from list
    config.label_callback = newLabelCallback