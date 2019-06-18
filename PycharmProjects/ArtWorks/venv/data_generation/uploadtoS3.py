import boto
import boto.s3
import os.path
import sys


src_dir = '/Users/ravikiranmandha/PycharmProjects/ArtWorks/ArtWorks-dataset/Artists/'
dest_dir = 'Artists'
# max size in bytes before uploading in parts. between 1 and 5 GB recommended
MAX_SIZE = 20 * 1000 * 1000
# size of parts when uploading in parts
PART_SIZE = 6 * 1000 * 1000


def upload_percent_cb(complete, total):
    sys.stdout.write('-')
    sys.stdout.flush()


def start_s3_upload_process():

    connection = boto.connect_s3(aws_access_key_id='your-aws-key',
                              aws_secret_access_key='your-aws-secret-key')
    my_bucket_name = "artworks-dataset"
    my_bucket = connection.get_bucket(my_bucket_name)
    if not my_bucket:
        print("bucket does not exits creating  bucket")
        my_bucket = connection.create_bucket(my_bucket_name)

    upload_file_names = []
    for path, subdir, files in os.walk(src_dir):
        # print "Path is ",  path, "\n Subdir is ", subdir,  "File is " ,files
        for filename in files:
            # upload_file_names.append(os.path.join(path, filename))
            upload_file_names.append(filename)


    for filename in upload_file_names:
        src_path = os.path.join(src_dir + filename)
        dest_path = os.path.join(dest_dir, filename)
        print('Uploading %s to Amazon S3 bucket %s' % (src_path, dest_path))

        file_size = os.path.getsize(src_path)
        if file_size > MAX_SIZE:
            print("Multi part upload")
            mp = my_bucket.initiate_multipart_upload(dest_path)
            with open(src_path, 'rb') as fp:
                while (fp.tell() < file_size):
                    fp_num += 1
                    print("uploading part %i" % fp_num)
                    mp.upload_part_from_file(fp, fp_num, cb=upload_percent_cb, num_cb=10, size=PART_SIZE)
                mp.complete_upload()
        else:
            k = boto.s3.key.Key(my_bucket)
            k.key = dest_path
            k.set_contents_from_filename(src_path, cb=upload_percent_cb, num_cb=10)


start_s3_upload_process()
