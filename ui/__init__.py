def __init__(self, topic_name, go_back, learn_topic):
    super().__init__()

    self.topic_name = topic_name
    self.go_back = go_back
    self.learn_topic_callback = learn_topic

    self.setup_ui()
