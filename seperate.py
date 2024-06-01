def split_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.read()
        logs = logs.split('agent=')
        
        analyst_logs = logs[2].split('task=')[1].split('2024')[0][:-4]
        researcher_logs = logs[4].split('task=')[1].split('2024')[0][:-4]
        recommender_logs = logs[6].split('task=')[1].split('2024')[0][:-4]

        # print('\n\nAnalyst logs:\n\n', analyst_logs)
        # print('\n\n\n\nResearcher logs:\n\n', researcher_logs)
        # print('\n\n\n\nRecommender logs:\n\n', recommender_logs)

        return analyst_logs, researcher_logs, recommender_logs


if __name__ == '__main__':
    split_logs('logs.txt')